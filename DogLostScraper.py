import pandas as pd
import sqlite3 as sql

scraper = pd.read_html("https://www.doglost.co.uk/dog-search.php?status=Lost")
scraped = pd.DataFrame(scraper[0])

conn = sql.connect("Lost_Dogs.db")
scraped.to_sql("DogLost", conn)
