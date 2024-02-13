from binance.client import Client
import config, json, talib
import websocket
import numpy as np
import telegramBot as tlg
from datetime import datetime


# Insere a criptomeda e seu intervalo de tempo gráfico
TRADE_SYMBOL = 'ADAUSDT'
TIME_INTERVAL = Client.KLINE_INTERVAL_1MINUTE
# TIME_INTERVAL = Client.KLINE_INTERVAL_15MINUTE
# TIME_INTERVAL = Client.KLINE_INTERVAL_1HOUR

# variável que armazena os valores de fechamento dos candles 
closes = []

def on_open(ws):
   print('Conexão iniciada')
   telegramBot.send_msg("Conexão iniciada")
def on_close(ws):
   print('Conexão Encerrada')
   telegramBot.send_msg("Conexão Encerrada")
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
      data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y - %Hh:%Mm')   
      print("--------------------------------------")
      telegramBot.send_msg("\n -------------------------------")
      telegramBot.send_msg("\n 🧩  " + data_e_hora_em_texto + "\n Moeda: " + str(TRADE_SYMBOL) + "\n Valor: " + str(close) )
      
      # Bandas de Bollinger
      if len(closes) > 21:
         upper, middle, lower = talib.BBANDS(np_closes, 21, 3, 3)
         BBSuperior = upper[-1]
         BBMedia = middle[-1]
         BBInferior = lower[-1]
         
      
      if ( (format(float(close),'.6f') < format(float(BBMedia),'.6f')) and (format(float(middle[-1]),'.6f') < format(float(middle[-3]),'.6f'))):
         telegramBot.send_msg("🔴 " + "Tendência de baixa - Média central inclinada para baixo")
         print("🔴 " + "Tendência de baixa - Média central inclinada para baixo")
         print("Close: ",close)
         print("Media-1 ",middle[-1])
         print("Media-3 ",middle[-3])
         
      elif ((format(float(close),'.8f') > format(float(BBMedia),'.8f') ) and (format(float(middle[-1]),'.8f') > format(float(middle[-3]),'.8f') )):
         telegramBot.send_msg("🟢 " + "Tendência de alta - Média central inclinada para cima")
         print("🟢 " + "Tendência de Alta - Média central inclinada para cima")
         print("Close: ",close)
         print("Media-1 ",middle[-1])
         print("Media-3 ",middle[-3])
         
      else:
         telegramBot.send_msg("🟡  " + "LATERALIDADE")
         print("🟡 " + "LATERALIDADE")
         print("Close: ",close)
         print("Media-1 ",middle[-1])
         print("Media-3 ",middle[-3])
            
         
      ### Que interessa
      if format(float(close),'.8f') < format(float(BBInferior),'.8f'):
         telegramBot.send_msg("🟢 " + "🟢 " +  "🟢 " + "🟢 " + "🟢 " +  "🟢 " +"\n Fechou abaixo da Bollinger \n !!!COMPRA" "\n Inferior: " + str(BBInferior) + "\n Close: " + str(format(float(close),'.8f')))
         
         print("Fechamento      :\t",format(float(close),'.6f'))
         print("inferior        :\t",format(float(BBInferior),'.8f'))
      
      elif format(float(close),'.8f') > format(float(BBSuperior),'.8f'):                             
         telegramBot.send_msg("🔴 " + "🔴 " + "🔴 " + "🔴 " + "🔴 " + "🔴 " + "🔴 " + "🔴 " + "🔴 " + data_e_hora_em_texto  + "\n Fechou acima da Bollinger \n !!!VENDA " + str(TRADE_SYMBOL) + "\n Fechamento: " + str(close) + "\n Superior:        " + str(BBSuperior) + "\n Fechamento > Superior !!!ÓTIMA VENDA")
         
         print("Fechamento      :\t",format(float(close),'.6f'))
         print("BBSuperior      :\t",format(float(BBSuperior),'.8f'))
      
           
            
         
if __name__ == "__main__":
   client = Client(config.API_KEY, config.API_SECRET)
   
   telegramBot = tlg.BotTelegram(config.TOKEN,config.CHAT_ID)
   
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
   
   