from binance.client import Client
import config, json, talib
import websocket
import numpy as np
import telegramBot as tlg
from datetime import datetime


# Insere a criptomeda e seu intervalo de tempo gráfico
TRADE_SYMBOL = 'GALAUSDT'
TIME_INTERVAL = Client.KLINE_INTERVAL_1MINUTE
# TIME_INTERVAL = Client.KLINE_INTERVAL_15MINUTE
# TIME_INTERVAL = Client.KLINE_INTERVAL_1HOUR

# variável que armazena os valores de fechamento dos candles 
closes = []

def on_open(ws):
   print('opened connection')

def on_close(ws):
   print('closed connection')

def on_message(ws, message):
   global closes

   json_message = json.loads(message)
   # print("linha 27:" + str(json_message))

   candle = json_message['k']
   
   
   is_candle_closed = candle['x']
   # print("linha 33: " + str(is_candle_closed))
   
   # armazeno valor de fechamento do candle
   close = candle['c']
   # print("linha 37 Fechamento: " + str(close))
   
   # verifica se o candle atual é fechamento  
   if is_candle_closed:
      
           
      closes.append(float(close))
      np_closes = np.array(closes)

      
      data_e_hora_atuais = datetime.now()
      data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y - %H:%M')   
      print("--------------------------------------")

      # Bandas de Bollinger
      if len(closes) > 21:
         upper, middle, lower = talib.BBANDS(np_closes, 21, 2, 2)
         last_BBupper = upper[-1]
         last_BBlower = lower[-1]
         last_BBmiddle = middle[-1]
     
      telegramBot.send_msg(data_e_hora_em_texto  + "\n Moeda: " + str(TRADE_SYMBOL) + "\n Fechamento: " + str(close) + "\n Superior:        " + str(last_BBupper) + "\n Media:            " + str( last_BBlower) + "\n Inferior:          " + str(last_BBmiddle))
     

   # Estocástico lento RSI
      if len(closes) > 21:
         fastk, fastd = talib.STOCHRSI(np_closes,timeperiod=21, fastk_period=21, fastd_period=3, fastd_matype=3) 
         last_SRSIk = fastk[-1]
         last_SRSId = fastd[-1]
         
      # Estocástico lento tradicional
      if len(closes) > 7:
         rsi = talib.RSI(np_closes, 8)
         last_RSI = rsi[-1]   
         telegramBot.send_msg("RSI: " + str(rsi) + "\n last_RSI" + str(last_RSI) + "\n lento_SRSIk" + str(last_SRSIk) + "\n lento_SRSId" + str(last_SRSId))
      
            
      
      if True:
         print("Date time       :\t",data_e_hora_em_texto)
         print("TRADE SYMBOL    :\t",TRADE_SYMBOL)
         print("Fechamento      :\t",format(float(close),'.6f'))
         print("Superior        :\t",format(float(last_BBupper),'.8f'))
         print("Média           :\t",format(float(last_BBlower),'.8f'))
         print("inferior        :\t",format(float(last_BBmiddle),'.8f'))
                                    
         telegramBot.send_msg("\n --------------------------------------")
   

if __name__ == "__main__":
   client = Client(config.API_KEY, config.API_SECRET)
   
   telegramBot = tlg.BotTelegram("6940071503:AAG2GhViUz-oLmKAZgu7oMg_ItlljYEgFbU","-4114868431")
   
   telegramBot.send_msg("=== Inicio do bot PyHbSinais ===")
     

   # retorna lista de valores OHLCV (Tempo de abertura, Abertura, Alta, Baixa, Fechamento,
   klines = client.get_historical_klines(TRADE_SYMBOL,TIME_INTERVAL, "1 day ago UTC")
   
   # Mostra status da conta
   status = client.get_account_status()
   telegramBot.send_msg("Status da conta:" + " " + str(status).replace("'data': ",""))

   klines = client.get_historical_klines(TRADE_SYMBOL,TIME_INTERVAL,"1 day ago UTC")

   for candles in range (len(klines) -1 ):
      closes.append(float(klines[candles][4]))
      
   SOCKET = "wss://stream.binance.com:9443/ws/"+TRADE_SYMBOL.lower()+"@kline_"+TIME_INTERVAL
   ws = websocket.WebSocketApp(SOCKET,on_open=on_open,on_close=on_close,on_message=on_message)
   ws.run_forever()
   
   