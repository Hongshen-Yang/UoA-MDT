# WebSocket API Client

import logging, time
from binance.lib.utils import config_logging
from binance.websocket.spot.websocket_api import SpotWebsocketAPIClient

# config_logging(logging, logging.DEBUG)

class WebsocketAPIClient:
    def __init__(self, api_key, api_secret, symbol, itvl, mode='testnet'):
        self.api_key=api_key
        self.api_secret=api_secret
        self.symbol=symbol
        self.itvl=itvl
        self.mode = mode
        self.api_url = self.get_api_url()
        config_logging(logging, logging.DEBUG)
        
    def get_api_url(self):
        # Mainnet API endpoint "wss://ws-api.binance.com:443/ws-api/v3" 443 port or 9443 port
        # Testnet API endpoint "wss://testnet.binance.vision/ws-api/v3"
        if self.mode == 'testnet':
            return "wss://testnet.binance.vision/ws-api/v3"
        elif self.mode == 'mainnet':
            return "wss://ws-api.binance.com:443/ws-api/v3"

    def on_close(_):
        logging.info("connection is closed")

    def message_handler(self, _, message):
        logging.info(message)

    def start(self):
        my_client = SpotWebsocketAPIClient(
            stream_url=self.get_api_url(),
            api_key=self.api_key,
            api_secret=self.api_secret,
            on_message=self.message_handler,
        )

        while True:
            command = input("Enter a command: ")
            if command == "stop":
                logging.info("closing ws connection")
                my_client.stop()
                break
            # Market
            elif command == "ping_connectivity":
                my_client.ping_connectivity()
            elif command == "server_time":
                my_client.server_time()
            elif command == "exchange_info":
                my_client.exchange_info()
            elif command == "order_book":
                my_client.order_book(self.symbol)
            elif command == "recent_trades":
                my_client.recent_trades(self.symbol)
            elif command == "historical_trades":
                my_client.historical_trades(self.symbol, self.api_key)
            elif command == "aggregate_trades":
                my_client.aggregate_trades(self.symbol)
            elif command == "klines":
                my_client.klines(symbol=self.symbol, interval=self.itvl)
            elif command == "ui_klines":
                my_client.ui_klines(symbol=self.symbol, interval=self.itvl)
            elif command == "avg_price":
                my_client.avg_price(symbol=self.symbol)
            elif command == "ticker_24hr":
                my_client.ticker_24hr()
            elif command == "ticker":
                my_client.ticker()
            elif command == "ticker_price":
                my_client.ticker_price()
            elif command == "ticker_book":
                my_client.ticker_book()
            # Account
            elif command == "account":
                my_client.account()
            # elif command == "order_rate_limit":
            #     my_client.order_rate_limit()
            elif command == "order_history":
                my_client.order_history()
            # elif command == "oco_history":
            #     my_client.oco_history()
            # elif command == "my_trades":
            #     my_client.my_trades(symbol=self.symbol, apiKey=self.api_key)
            # elif command == "prevented_matches":
            #     my_client.prevented_matches(symbol=self.symbol)
            # Trade
            elif command == "new_order":
                my_client.new_order()
            elif command == "new_order_test":
                my_client.new_order_test()
            elif command == "get_order":
                my_client.get_order()
            elif command == "cancel_order":
                my_client.cancel_order()
            elif command == "cancel_replace_order":
                my_client.cancel_replace_order()
            elif command == "get_open_orders":
                my_client.get_open_orders()
            elif command == "cancel_open_orders":
                my_client.cancel_open_orders()
            elif command == "new_oco_order":
                my_client.new_oco_order()
            elif command == "get_oco_order":
                my_client.get_oco_order()
            elif command == "cancel_oco_order":
                my_client.cancel_oco_order()
            elif command == "get_open_oco_orders":
                my_client.get_open_oco_orders()
            # User Data Stream
            elif command == "user_data_start":
                my_client.user_data_start()
            elif command == "user_data_ping":
                my_client.user_data_ping()
            elif command == "user_data_stop":
                my_client.user_data_stop()
            
            # Add more commands for other sections (Account, Trade, User Data Stream) here.
            
            else:
                logging.error("""
                    Command error, please use the following commands:

                    # Market
                    ping_connectivity, server_time, exchange_info, order_book, recent_trades, historical_trades, aggregate_trades, klines, ui_klines, avg_price, ticker_24hr, ticker, ticker_price, ticker_book

                    # Account
                    account, order_rate_limit, order_history, oco_history, my_trades, prevented_matches

                    # Trade
                    new_order, new_order_test, get_order, cancel_order, cancel_replace_order, get_open_orders, cancel_open_orders, new_oco_order, get_oco_order, cancel_oco_order, get_open_oco_orders
                    
                    # User Data Stream
                    user_data_start, user_data_ping, user_data_stop
                """)


if __name__ == "__main__":
    client = WebsocketAPIClient()
    client.start()