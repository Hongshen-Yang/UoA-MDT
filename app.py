import asyncio, sqlite3
from mdt_utils import get_api_key
from mdt_bnws import client_stream, client_api

async def clear_db():
    # Connect to SQLite database
    conn = sqlite3.connect('sqlite.db')
    cursor = conn.cursor()
    # Delete existing data from kline table
    cursor.execute('DELETE FROM kline;')
    conn.commit()
    conn.close()

async def main():
    api_key, api_secret = get_api_key()
    await clear_db()
    client_stream()

if __name__ == "__main__":
    asyncio.run(main())