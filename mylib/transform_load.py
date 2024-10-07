"""
Transforms and Loads data into the local SQLite3 database
Example:
country,beer_servings,spirit_servings,wine_servings,total_litres_of_pure_alcohol
"""
import sqlite3
import csv
import os

#load the csv file and insert into a new sqlite3 database
def load(dataset="data/drinks.csv"):
    """"Transforms and Loads data into the local SQLite3 database"""

    #prints the full working directory and path
    print(os.getcwd())
    payload = csv.reader(open(dataset, newline=''), delimiter=',')
    conn = sqlite3.connect('DrinksDB.db')
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS DrinksDB")
    c.execute("CREATE TABLE DrinksDB \
              (country,beer_servings,spirit_servings,wine_servings,total_litres_of_pure_alcohol)")
    #insert
    c.executemany("INSERT INTO DrinksDB VALUES (?, ?, ?, ?, ?)", payload)
    conn.commit()
    conn.close()
    return "DrinksDB.db"

