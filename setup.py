from setuptools import setup, find_packages

setup(
    name='structured_rag',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'sqlalchemy',
        'openai',
        'psycopg2',
        'mysql-connector-python'
    ],
    entry_points={
        'console_scripts': [
            'rag_utility=structured_rag.rag:main'
        ]
    }
)
