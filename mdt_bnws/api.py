# WebSocket API Client

import logging, time
from binance.lib.utils import config_logging
from binance.websocket.spot.websocket_api import SpotWebsocketAPIClient

config_logging(logging, logging.DEBUG)

def on_close(_):
    logging.info("connection is closed")

def message_handler(_, message):
    logging.info(message)

# Base endpoint "wss://ws-api.binance.com:443/ws-api/v3"
# Testnet base endpoint "wss://testnet.binance.vision/ws-api/v3"
# Base stream wss://stream.binance.com:9443

def client_api(api_key, api_secret):
    my_client = SpotWebsocketAPIClient(
        stream_url="wss://testnet.binance.vision/ws-api/v3",
        api_key=api_key,
        api_secret=api_secret,
        on_message=message_handler,
    )

    my_client.ticker(symbol="BNBBUSD", type="FULL")

    time.sleep(5)

    logging.info("closing ws connection")
    my_client.stop()

