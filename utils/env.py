from configparser import ConfigParser

def get_api_key():
    config = ConfigParser()
    config.read("config.ini")
    return config["keys"]["api_key"], config["keys"]["api_secret"]