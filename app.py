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
<<<<<<< HEAD
    client_stream(itvl='1s')
=======
    client_stream()
>>>>>>> d25214eb98ef15a456e4e14c93106a01f6411c75

if __name__ == "__main__":
    asyncio.run(main())