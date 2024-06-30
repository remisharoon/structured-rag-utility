import unittest
from structured_rag.rag import RAGUtility
import json

class TestRAGUtility(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config_path = 'test_config.json'
        with open(cls.config_path, 'w') as file:
            json.dump({
                "database": {"url": "sqlite:///:memory:"},
                "openai": {"api_key": "test-api-key"}
            }, file)
        cls.rag_utility = RAGUtility(cls.config_path)
        cls.create_test_db()

    @classmethod
    def tearDownClass(cls):
        import os
        os.remove(cls.config_path)

    @classmethod
    def create_test_db(cls):
        engine = cls.rag_utility.engine
        with engine.connect() as connection:
            connection.execute(text('''CREATE TABLE employees (
                id INTEGER PRIMARY KEY,
                name TEXT,
                join_date TEXT
            )'''))
            connection.execute(text('''INSERT INTO employees (name, join_date) VALUES
                ('Alice', '2023-01-15'),
                ('Bob', '2023-02-20')
            '''))

    def test_fetch_records(self):
        records = self.rag_utility.fetch_records('SELECT * FROM employees')
        self.assertEqual(len(records), 2)

    def test_generate_response(self):
        prompt = "What is the capital of France?"
        response = self.rag_utility.generate_response(prompt)
        self.assertIsInstance(response, str)

if __name__ == '__main__':
    unittest.main()
