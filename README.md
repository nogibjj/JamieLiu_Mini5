# JamieLiu_Mini5

[![CI](https://github.com/nogibjj/JamieLiu_Mini5/actions/workflows/ci.yml/badge.svg)](https://github.com/nogibjj/JamieLiu_Mini5/actions/workflows/ci.yml)

**This repository handles the ETL (Extract, Transform, Load) process and querying operations on a drinks dataset**. The dataset consists of information about various countries, including the number of beer, spirit, and wine servings, and total liters of pure alcohol consumed. The project allows users to extract data, load it into an SQLite database, and perform various queries such as creating, updating, and deleting records.

## Project Structure

```bash
.
├── .devcontainer/
├── .github/workflows/
│   └── ci.yml
├── data/
│   └── drinks.csv
├── env/
├── mylib/
│   ├── __init__.py
│   ├── extract.py
│   ├── query.py
│   └── transform_load.py
├── .gitignore
├── Dockerfile
├── drinks_query_log.md
├── DrinksDB.db
├── LICENSE
├── main.py              # Main CLI script to execute different operations
├── Makefile             # Automates build, test, and clean commands
├── README.md
├── requirements.txt
├── setup.sh
└── test_main.py         # Test cases to ensure the functionality of main.py
```

## Features

- **Extract**: Fetch the `drinks.csv` dataset and log the operation.
- **Transform and Load**: Transform the CSV data and load it into an SQLite database.
- **CRUD Operations**: Perform `Create`, `Read`, `Update`, and `Delete` operations on the dataset.
- **SQL Query Logging**: Logs every SQL query executed to a markdown file (`drinks_query_log.md`).
- **Tests**: Test various operations such as extracting, transforming, querying, and database operations.

## Setup

1. **Clone the repository:**
   ```bash
   git clone git@github.com:nogibjj/JamieLiu_Mini5.git
   cd JamieLiu_Mini5
   ```
2. **Install project dependencies:**
   ```bash
   make install
   ```
3. **Format the code:**

   ```bash
   make format
   ```

4. **Run linting checks:**

   ```bash
   make lint
   ```

5. **Run tests:**

   ```bash
   make test
   ```

6. **Run all steps (Install, Format, Lint, Test):**
   ```bash
   make all
   ```

## CRUD Operations

- **Extract the data:**

  ```bash
  python main.py extract
  ```

- **Transform and load the data into the database:**

  ```bash
  python main.py transform_load
  ```

- **Create a new record:**

  ```bash
  python main.py create_record "Germany" 300 200 150 12.5
  ```

- **Update an existing record:**

  ```bash
  python main.py update_record "Germany" 320 210 160 13.0
  ```

- **Delete a record:**

  ```bash
  python main.py delete_record "Germany"
  ```

- **Run a custom SQL query:**

  ```bash
  python main.py general_query "SELECT * FROM DrinksDB WHERE country = 'Germany'"
  ```

- **Read all data from the database:**

  ```bash
  python main.py read_data
  ```

## Logging

All executed SQL queries are logged in the `drinks_query_log.md` file for future reference.
