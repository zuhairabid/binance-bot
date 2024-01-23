from binance.client import Client




# Replace with your own API key and secret
api_key = "pax9KSXt9hwBai4cj52qZE9RqMxaXrWMHJRWVgCH9Uxt7d9iUWNlZMFmn9XhLIMJ"
api_secret = "5E2KVAZypXtSUrQgYoTUn9IpzLZoQ80Mztg9dx0UQMboX9fP8jQBRULKeJDxpo6h"


# Create a client object
client = Client(api_key, api_secret, testnet=False)

def check_buy_sl_tp(symbol,side,quantity,price,stop_loss_price,take_profit_price):
    while True:
        print("Waiting for buy SL TP")
        time.sleep(60/1200)
        current_price = float(client.futures_symbol_ticker(symbol=symbol)['price'])
        if current_price >= take_profit_price:
            close_order = client.futures_create_order(
                        symbol=symbol,
                        side="SELL",
                        type="MARKET",
                        quantity=quantity,
                        positionSide="LONG"
                    )
            print("""
                  
                  ////////////////////////////
                  
                  Reached by Take Profit
                  
                  ///////////////////////////
                  """)
            break
        elif current_price <= stop_loss_price:
            close_order = client.futures_create_order(
                            symbol=symbol,
                            side="SELL",
                            type="MARKET",
                            quantity=quantity,
                            positionSide="LONG"
                        )
            print("""
                  
                  ////////////////////////////
                  
                  Reached by Stop Loss
                  
                  ///////////////////////////
                  """)
            break
        
    return True


def check_sell_sl_tp(symbol,side,quantity,price,stop_loss_price,take_profit_price):
    while True:
        print("Waiting for sell SL TP")
        time.sleep(60/1200)
        current_price = float(client.futures_symbol_ticker(symbol=symbol)['price'])
        if current_price >= stop_loss_price:
            close_order = client.futures_create_order(
                        symbol=symbol,
                        side="BUY",
                        type="MARKET",
                        quantity=quantity,
                        positionSide="SHORT"
                    )
            print("""
                  
                  ////////////////////////////
                  
                  Reached by Stop Loss
                  
                  ///////////////////////////
                  """)
            break
        elif current_price <= take_profit_price:
            close_order = client.futures_create_order(
                            symbol=symbol,
                            side="BUY",
                            type="MARKET",
                            quantity=quantity,
                            positionSide="SHORT"
                        )
            print("""
                  
                  ////////////////////////////
                  
                  Reached by Take Profit
                  
                  ///////////////////////////
                  """)
            break
        
    return True



import time
def start_trade(symbol,side,quantity,price,stop_loss_price,take_profit_price):
    trade_finished = False
    price_when_trade_started = float(client.futures_symbol_ticker(symbol=symbol)['price'])
    print("Started Trade Price: ",price_when_trade_started)
    while not trade_finished:
        time.sleep(60/1200)
        current_price = float(client.futures_symbol_ticker(symbol=symbol)['price'])
        print("Current Price: ",current_price)
        if price<price_when_trade_started:
            print(f"Target Limit Condition: <= {price}")
            if current_price >= price:
                print("Reached Target Limit")
                # trade
                # //////////////////
                if side == 'BUY':
                    buy_order = client.futures_create_order(
                                symbol=symbol,
                                side="BUY",
                                type="MARKET",
                                quantity=quantity,
                                positionSide="LONG"
                    )
                    trade_finished = check_buy_sl_tp(symbol,side,quantity,price,stop_loss_price,take_profit_price)
                elif side == 'SELL':
                    sell_order = client.futures_create_order(
                                symbol=symbol,
                                side="SELL",
                                type="MARKET",
                                quantity=quantity,
                                positionSide="SHORT"
                    )
                    trade_finished = check_sell_sl_tp(symbol,side,quantity,price,stop_loss_price,take_profit_price)
                    
                # //////////////////
                pass
        elif price>price_when_trade_started:
            print(f"Target Limit Condition: >= {price}")
            if current_price >= price:
                print("Reached Target Limit")
                # trade
                # //////////////////
                if side == 'BUY':
                    buy_order = client.futures_create_order(
                                symbol=symbol,
                                side="BUY",
                                type="MARKET",
                                quantity=quantity,
                                positionSide="LONG"
                    )
                    trade_finished = check_buy_sl_tp(symbol,side,quantity,price,stop_loss_price,take_profit_price)
                elif side == 'SELL':
                    sell_order = client.futures_create_order(
                                symbol=symbol,
                                side="SELL",
                                type="MARKET",
                                quantity=quantity,
                                positionSide="SHORT"
                    )
                    trade_finished = check_sell_sl_tp(symbol,side,quantity,price,stop_loss_price,take_profit_price)
                    
                # //////////////////
                pass
        elif price_when_trade_started == price:
            # trade
                # //////////////////
            if side == 'BUY':
                buy_order = client.futures_create_order(
                            symbol=symbol,
                            side="BUY",
                            type="MARKET",
                            quantity=quantity,
                            positionSide="LONG"
                )
                trade_finished = check_buy_sl_tp(symbol,side,quantity,price,stop_loss_price,take_profit_price)
            elif side == 'SELL':
                sell_order = client.futures_create_order(
                            symbol=symbol,
                            side="SELL",
                            type="MARKET",
                            quantity=quantity,
                            positionSide="SHORT"
                )
                trade_finished = check_sell_sl_tp(symbol,side,quantity,price,stop_loss_price,take_profit_price)
                    
                # //////////////////
    
    
symbol = input("Enter Symbol: ")
side = input("Enter Side: ")
quantity = float(input("Enter Quantity: "))
price = float(input("Enter Price: "))
stop_loss_price = float(input("Enter Stop Loss Price: "))
take_profit_price = float(input("Enter Take Profit Price: "))

while True:
    start_trade(symbol,side,quantity,price,stop_loss_price,take_profit_price)
