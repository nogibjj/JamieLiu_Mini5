"""Query the database"""

import sqlite3

# Define a global variable for the log file
LOG_FILE = "drinks_query_log.md"


def log_query(query):
    """Adds a query to the query log file."""
    with open(LOG_FILE, "a") as file:
        file.write(f"```sql\n{query}\n```\n\n")


def general_query(query):
    """Runs a query a user inputs."""
    with sqlite3.connect("DrinksDB.db") as conn:
        cursor = conn.cursor()
        cursor.execute(query)

        if query.strip().lower().startswith(("insert", "update", "delete")):
            conn.commit()

        if query.strip().lower().startswith("select"):
            data = cursor.fetchall()
            return data

        cursor.close()

    log_query(f"{query}")


def create_record(country, 
                  beer_servings, 
                  spirit_servings, 
                  wine_servings, 
                  total_alcohol):
    """Create a new record in the drinks dataset."""
    conn = sqlite3.connect("DrinksDB.db")
    c = conn.cursor()
    c.execute(
        """
        INSERT INTO DrinksDB 
        (country, 
        beer_servings, 
        spirit_servings, 
        wine_servings, 
        total_litres_of_pure_alcohol) 
        VALUES (?, ?, ?, ?, ?)
        """,
        (country, beer_servings, spirit_servings, wine_servings, total_alcohol),
    )
    conn.commit()
    conn.close()

    # Log the query
    log_query(
        f"""INSERT INTO DrinksDB VALUES (
            '{country}', 
            {beer_servings}, 
            {spirit_servings}, 
            {wine_servings}, 
            {total_alcohol});"""
    )


def update_record(country, 
                  beer_servings, 
                  spirit_servings, 
                  wine_servings, 
                  total_alcohol):
    """Update a record in the drinks dataset based on the country."""
    conn = sqlite3.connect("DrinksDB.db")
    c = conn.cursor()
    c.execute(
        """
        UPDATE DrinksDB 
        SET beer_servings=?, 
        spirit_servings=?, 
        wine_servings=?, 
        total_litres_of_pure_alcohol=?
        WHERE country=?
        """,
        (
            beer_servings,
            spirit_servings,
            wine_servings,
            total_alcohol,
            country,
        ),
    )
    conn.commit()
    conn.close()

    # Log the query
    log_query(
        f"""UPDATE DrinksDB SET 
        beer_servings={beer_servings},
        spirit_servings={spirit_servings}, 
        wine_servings={wine_servings}, 
        total_litres_of_pure_alcohol={total_alcohol} 
        WHERE country='{country}';"""
    )


def delete_record(country):
    """Delete a record from the drinks dataset based on the country."""
    conn = sqlite3.connect("DrinksDB.db")
    c = conn.cursor()
    c.execute("DELETE FROM DrinksDB WHERE country=?", (country,))
    conn.commit()
    conn.close()

    # Log the query
    log_query(f"DELETE FROM DrinksDB WHERE country='{country}';")


def read_data():
    """Read data from the drinks dataset."""
    conn = sqlite3.connect("DrinksDB.db")
    c = conn.cursor()
    c.execute("SELECT * FROM DrinksDB")
    data = c.fetchall()
    log_query("SELECT * FROM DrinksDB;")
    return data
