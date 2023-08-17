# WebSocket stream Client

import logging, time, json, sqlite3
# from ..utils.env import get_api_key
from binance.lib.utils import config_logging
from binance.websocket.spot.websocket_stream import SpotWebsocketStreamClient

# api_key, api_secret = get_api_key()

# Configure logging
config_logging(logging, logging.DEBUG)

def on_close(_):
    conn.close()
    logging.info("connection is closed")

def message_handler(_, message):
    mes = json.loads(message)
    
    if 'k' in mes:
        if mes['k']['x']==True:

            conn = sqlite3.connect('sqlite.db')
            cursor = conn.cursor()

            insert_query = '''
            INSERT INTO kline (start_time, close_time, symbol, interval, first_id, last_id, open, close, high, low,
            base_vol, num_trades, closed, quote_vol, taker_base_vol, taker_quote_vol, ignore)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            '''
            conn.execute(insert_query, tuple(mes['k'].values()))
            conn.commit()
            conn.close()

            logging.info(mes['k'])
    else:
        logging.info(mes)

# Base API endpoint "wss://ws-api.binance.com:443/ws-api/v3"
# Testnet API endpoint "wss://testnet.binance.vision/ws-api/v3"
# Base stream wss://stream.binance.com:9443 or wss://stream.binance.com:443
# Testnet stream endpoint "wss://testnet.binance.vision"

def client_stream():

    my_client = SpotWebsocketStreamClient(
        stream_url="wss://stream.binance.com:443",
        on_message=message_handler,
        on_close=on_close
    )

    # Response can be found
    # https://github.com/binance/binance-spot-api-docs/blob/master/user-data-stream.md

    # my_client.agg_trade(symbol="btcusdt")
    # my_client.book_ticker(symbol="btcusdt")
    # my_client.diff_book_depth(symbol="btcusdt", speed=1000)
    # my_client.rolling_window_ticker("BNBUSDT", "1h")
    my_client.kline(symbol="btcusdt", interval="1s")
    # my_client.trade(symbol="btcusdt")
    # my_client.ticker(symbol="btcusdt")

if __name__ == "__main__":
    client_stream()