from oanda_api import OandaAPI

api = OandaAPI()

while True:
    command = input("Enter command:")
    if command == "T":
        print("Make a Trade")
        trade_id = api.place_trade("EUR_USD", 1000, take_profit=1.097, stop_loss=1.088, )
        print('trade_id', trade_id)
    if command == "Q":
        break
