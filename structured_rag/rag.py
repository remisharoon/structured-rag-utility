from sqlalchemy import create_engine, text, MetaData, Table
from sqlalchemy.engine import Engine
from typing import List, Dict, Any
import openai
import json


class RAGUtility:
    def __init__(self, config_path: str):
        with open(config_path, 'r') as file:
            config = json.load(file)
        self.engine: Engine = create_engine(config['database']['url'])
        openai.api_key = config['openai']['api_key']
        self.metadata = MetaData()
        self.metadata.reflect(bind=self.engine)

    def fetch_records(self, query: str) -> List[Dict[str, Any]]:
        with self.engine.connect() as connection:
            result = connection.execute(text(query))
            columns = result.keys()
            return [dict(zip(columns, row)) for row in result]

    def generate_response(self, prompt: str) -> str:
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()

    def generate_sql_query(self, input_query: str) -> str:
        # List all table names and their columns to help the LLM generate the correct SQL query
        tables_info = "\n".join(
            [f"Table {table.name}: " + ", ".join([column.name for column in table.columns])
             for table in self.metadata.sorted_tables]
        )

        prompt = f"""
        The following are the available tables and their columns:
        {tables_info}

        Based on this schema, generate an SQL query for the following request:
        {input_query}
        """
        response = self.generate_response(prompt)
        return response

    def rag_process(self, input_query: str) -> str:
        sql_query = self.generate_sql_query(input_query)
        records = self.fetch_records(sql_query)
        records_str = '\n'.join([str(record) for record in records])
        final_prompt = f"{input_query}\n\nHere are the records:\n{records_str}\n\nPlease generate a response based on these records."
        return self.generate_response(final_prompt)


if __name__ == "__main__":
    config_path = 'config.json'
    input_query = 'What are the details of employees who joined in 2023?'

    rag_utility = RAGUtility(config_path)
    response = rag_utility.rag_process(input_query)
    print(response)
