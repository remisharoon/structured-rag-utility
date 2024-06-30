# Structured RAG Utility

**Structured RAG Utility** is a flexible, generic Retrieval-Augmented Generation (RAG) tool designed to fetch structured data from various relational databases and generate responses using Language Models (LLMs). This library supports multiple database types through SQLAlchemy and offers easy configuration, making it a powerful addition to any data-driven application.

### Features

- **Multi-Database Support**: Connect to SQLite, PostgreSQL, MySQL, and other databases using SQLAlchemy.
- **Configurable**: Simple configuration via a JSON file for database and API settings.
- **Integration with OpenAI**: Utilize OpenAI's API to generate responses based on retrieved data.
- **Unit Tests**: Ensure reliability and correctness with comprehensive unit tests.
- **Documentation**: Detailed usage instructions and examples provided.

### Getting Started

1. **Clone the repository**:

   \```bash
   git clone https://github.com/remisharoon/structured-rag-utility.git
   cd structured-rag-utility
   \```

2. **Install dependencies**:

   \```bash
   pip install -r requirements.txt
   \```

3. **Configure your settings**:

   Create a `config.json` file in the root directory with your database URL and OpenAI API key.

4. **Run the utility**:

   \```bash
   python structured_rag/rag.py
   \```

### Usage

Modify the `config.json`, `input_query`, and `sql_query` variables in `structured_rag/rag.py` to fit your specific needs.

### Testing

Run unit tests with:

\```bash
python -m unittest discover tests
\```

### License

This project is licensed under the MIT License.
