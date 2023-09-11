import asyncio, sqlite3
from mdt_utils import get_api_key
from mdt_bnws import WebsocketStreamClient, WebsocketAPIClient

async def clear_db():
    # Connect to SQLite database
    conn = sqlite3.connect('sqlite.db')
    cursor = conn.cursor()
    # Delete existing data from kline table
    cursor.execute('DELETE FROM kline;')
    conn.commit()
    conn.close()

async def main(symbol='BTCUSDT', itvl='1s', mode='mainnet'):
    api_key, api_secret = get_api_key()

    stream_client = WebsocketStreamClient(symbol=symbol, itvl=itvl, mode=mode)
    await clear_db()
    stream_client.start_stream()

    # api_client = WebsocketAPIClient(api_key, api_secret, symbol=symbol, itvl=itvl, mode=mode)
    # api_client.start()

if __name__ == "__main__":
    asyncio.run(main())