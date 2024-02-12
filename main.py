from binance.client import Client
import config

if __name__ == "__main__":
   client = Client(config.API_KEY, config.API_SECRET)