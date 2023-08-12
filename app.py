import sqlite3
from utils import get_api_key
from bnws import client_stream, client_api

api_key, api_secret = get_api_key()

# Connect to SQLite database
conn = sqlite3.connect('sqlite.db')
cursor = conn.cursor()
# Delete existing data from kline table
cursor.execute('DELETE FROM kline;')
conn.commit()
conn.close()

client_stream()
