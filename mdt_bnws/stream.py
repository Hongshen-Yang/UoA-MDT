# WebSocket stream Client

import logging, datetime, time, json, sqlite3, random, matplotlib
from binance.lib.utils import config_logging
from binance.websocket.spot.websocket_stream import SpotWebsocketStreamClient
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')

class WebsocketStreamClient:
    def __init__(self, symbol, itvl='1s',  mode='mainnet'):
        self.itvl = itvl
        self.mode = mode
        self.symbol = symbol
        self.stream_url = self.get_stream_url()
        # Initialize empty data lists
        self.plot_x = []
        self.plot_y = []

        # Create a Matplotlib figure and axis
        self.fig, self.ax = plt.subplots()
        
        config_logging(logging, logging.DEBUG)

    def get_stream_url(self):
        # Mainnet stream endpoint wss://stream.binance.com:9443 or wss://stream.binance.com:443
        # Testnet stream endpoint "wss://testnet.binance.vision"
        if self.mode == 'testnet':
            return "wss://testnet.binance.vision"
        elif self.mode == 'mainnet':
            return "wss://stream.binance.com:9443"
    
    def on_close(self, _):
        self.conn.close()
        logging.info("Connection is closed")
    
    def update_chart(self, kline_data):
        self.plot_x.append(datetime.datetime.fromtimestamp(kline_data['t']/1000.0))
        self.plot_y.append(float(kline_data['c']))

        self.ax.clear()
        self.ax.plot(self.plot_x, self.plot_y, label='Closing Price')
    
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Closing Price')
        self.ax.legend()
        # TODO: tilt the axis 45 degree, and show the time in HH:MM:SS format, not in scientific notation

        plt.show()
    
    def message_handler(self, _, message):
        mes = json.loads(message)
        
        if 'k' in mes and mes['k']['x']:
            self.insert_kline_data(mes['k'])
            self.update_chart(mes['k'])
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
        # logging.info(kline_data)
    
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
        my_client.kline(symbol=self.symbol, interval=self.itvl)
        # my_client.trade(symbol="btcusdt")
        # my_client.ticker(symbol="btcusdt")

        # Keep the Matplotlib code in the main thread
        plt.show()  # Display the Matplotlib chart

if __name__ == "__main__":
    client = WebsocketStreamClient(symbol='BTCUSDT')
    client.start_stream()