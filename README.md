# UoA-MDT

This is a coding project for a quantitative trading bot based on [Binance Exchange](https://www.binance.com/en).

## Prerequisites
Before you dive into setting up and using the Trading Bot, make sure you have your API Keys ready. Here's how you can obtain them:
1. **Create API Keys on Binance**: To begin, generate a pair of API Keys on Binance. Follow this guide to create your keys: [How to Create API Keys on Binance](https://www.binancezh.top/en/support/faq/how-to-create-api-keys-on-binance-360002502072)
2. **Configure API Keys:**: Once you have your API Keys, create a `config.ini` file in the root directory of this project. Populate the file with your API Key and API Secret as shown below:
```ini
[keys]
api_key = [your API key]
api_secret = [your API secret]
```
## Getting Started

To start using the UoA-MDT Trading Bot, you need to follow a few steps:

1. **Build the Docker Image**: Execute the following command to build the Docker image for the trading bot:
```bash
docker build -t uoa-mdt .
```
2.Run the Docker Container: Once the image is built, run the Docker container using this command:
```
docker run -it --rm uoa-mdt
```
And that's it! You're now ready to explore the capabilities of the UoA-MDT Quantitative Trading Bot.
