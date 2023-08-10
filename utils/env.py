from configparser import ConfigParser

def get_api_key():
    config = ConfigParser()
    config.read("config.ini")
    return config["keys"]["api_key"], config["keys"]["api_secret"]

    # config.ini
    #
    # [keys]
    # api_key=abc123456
    # api_secret=cba654321
    #
    # You can create your API key by following the tutorial from Binance "How to Create API Keys on Binance"
    # https://www.binance.com/en/support/faq/how-to-create-api-keys-on-binance-360002502072