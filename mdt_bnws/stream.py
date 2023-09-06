# WebSocket stream Client

import logging, time, json, sqlite3
# from ..utils.env import get_api_key
from binance.lib.utils import config_logging
from binance.websocket.spot.websocket_stream import SpotWebsocketStreamClient

# Configure logging
config_logging(logging, logging.DEBUG)

class WebSocketStreamClient:
    def __init__(self, itvl='1s', mode='mainnet'):
        self.itvl = itvl
        self.mode = mode
        self.stream_url = self.get_stream_url()
        config_logging(logging, logging.DEBUG)
        
    def get_stream_url(self):
        # Base API endpoint "wss://ws-api.binance.com:443/ws-api/v3"
        # Testnet API endpoint "wss://testnet.binance.vision/ws-api/v3"
        # Base stream wss://stream.binance.com:9443 or wss://stream.binance.com:443
        # Testnet stream endpoint "wss://testnet.binance.vision"
        if self.mode == 'testnet':
            return "wss://testnet.binance.vision"
        elif self.mode == 'mainnet':
            return "wss://stream.binance.com:9443"
    
    def on_close(self, _):
        self.conn.close()
        logging.info("Connection is closed")
    
    def message_handler(self, _, message):
        mes = json.loads(message)
        
        if 'k' in mes and mes['k']['x']:
            self.insert_kline_data(mes['k'])
        else:
            logging.info(mes)
    
    def insert_kline_data(self, kline_data):
        conn = sqlite3.connect('sqlite.db')
        cursor = conn.cursor()
        
        insert_query = '''
        INSERT INTO kline (start_time, close_time, symbol, interval, first_id, last_id, open, close, high, low,
        base_vol, num_trades, closed, quote_vol, taker_base_vol, taker_quote_vol, ignore)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''
        conn.execute(insert_query, tuple(kline_data.values()))
        conn.commit()
        conn.close()
        logging.info(kline_data)
    
    def start_stream(self):
        my_client = SpotWebsocketStreamClient(
            stream_url=self.stream_url,
            on_message=self.message_handler,
            on_close=self.on_close
        )
        
        # Response can be found
        # https://github.com/binance/binance-spot-api-docs/blob/master/user-data-stream.md

        # my_client.agg_trade(symbol="btcusdt")
        # my_client.book_ticker(symbol="btcusdt")
        # my_client.diff_book_depth(symbol="btcusdt", speed=1000)
        # my_client.rolling_window_ticker("BNBUSDT", "1h")
        my_client.kline(symbol="btcusdt", interval=self.itvl)
        # my_client.trade(symbol="btcusdt")
        # my_client.ticker(symbol="btcusdt")

if __name__ == "__main__":
    client = WebSocketStreamClient()
    client.start_stream()