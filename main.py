from binance.client import Client
import config, json, talib
import websocket
import numpy as np
import telegramBot as tlg
from datetime import datetime


# Insere a criptomeda e seu intervalo de tempo gráfico
# TRADE_SYMBOL = 'ADAUSDT'
TRADE_SYMBOL = 'MATICUSDT'
# TRADE_SYMBOL = 'MANAUSDT'
# TRADE_SYMBOL = 'AXSUSDT'
# TRADE_SYMBOL = 'SEIUSDT'
# TRADE_SYMBOL = 'ETHUSDT'
# TRADE_SYMBOL = 'BTCUSDT'
# TRADE_SYMBOL = 'CHZUSDT'
# TRADE_SYMBOL = 'LINKUSDT'
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
      print("CRYPTO         :\t",TRADE_SYMBOL)
      print("Closed value   :\t",format(float(close),'.6f'))
      
      telegramBot.send_msg("\n -------------------------------")
      telegramBot.send_msg("\n 🧩  " + data_e_hora_em_texto
                              +"\n*Tempo Gráfico: {}*".format(TIME_INTERVAL) 
                              +"\n*= CRYPTO {}* =".format(TRADE_SYMBOL)
                              +"\n*VALOR: {}* ".format(float(close),'.6f'))
      
      # Bandas de Bollinger
      if len(closes) > 21:
         upper, middle, lower = talib.BBANDS(np_closes, 21, 3, 3)
         BBSuperior = upper[-1]
         BBMedia = middle[-1]
         BBInferior = lower[-1]
         
      # Se máxima maior que banda superior
      if (format(float(candle['h']),'.6f') > format(float(BBSuperior),'.6f')):
        telegramBot.send_msg("=== *VENDER {}* ===".format(TRADE_SYMBOL)
               +"\n♨️Máxima *ACIMA* da Bollinger ♨️"
               +"\nBollinger Superior......."+str(format(float(BBSuperior),'.5f'))
               +"\n*Máxima*............"+str(format(float(close),'.5f'))) 
         
         # Se mínima menor que banda inferior
      if (format(float(candle['h']),'.6f') < format(float(BBInferior),'.8f')):
         telegramBot.send_msg("=== *COMPRAR {}* ===".format(TRADE_SYMBOL)
               +"\n🛤️ *Mínima *ABAIXO* da banda inferior* 🛤️"
               +"\nFechou ABAIXO da Bollinger"                
               +"\nBollinger Inferior.............."+str(format(float(BBInferior),'.6f'))
               +"\nFechamento..........."+str(format(float(close),'.6f')))
         
         # Se fechamento entre a media central
      if ((format(float(candle['h']),'.6f') > format(float(BBMedia),'.6f')) and (format(float(candle['h']),'.6f') < format(float(BBMedia),'.8f'))):
         telegramBot.send_msg("🟡 *+++ LATERALIDADE +++ 🟡{}*".format(TRADE_SYMBOL))
         print("Fechamento próximo a media central")
                     
         
      ### Que interessa
      if format(float(close),'.8f') < format(float(BBInferior),'.8f'):
         telegramBot.send_msg("=== *COMPRAR {}* ===".format(TRADE_SYMBOL)
               +"\n 🟢  🟢  🟢  🟢  🟢  🟢  🟢  🟢" + data_e_hora_em_texto
               +"\nTempo Gráfico: " +str(TIME_INTERVAL)
               +"\nFechou ABAIXO da Bollinger"                
               +"\nBBInferior.............."+str(format(float(BBInferior),'.6f'))
               +"\nBBSuperior.............."+str(format(float(BBSuperior),'.6f')))
         
         print("Fechamento      :\t",format(float(close),'.6f'))
         print("inferior        :\t",format(float(BBInferior),'.8f'))
      
      elif format(float(close),'.8f') > format(float(BBSuperior),'.8f'):                             
         telegramBot.send_msg("=== *VENDER {}* ===".format(TRADE_SYMBOL)
               +"\n 🔴  🔴  🔴  🔴  🔴  🔴  🔴  🔴"
               + data_e_hora_em_texto
               +"\nTempo Gráfico: " +str(TIME_INTERVAL)
               +"\nFechou ACIMA da Bollinger"
               +"\nBBSuperior.............."+str(format(float(BBSuperior),'.6f'))
               +"\nFechamento............"+str(format(float(close),'.6f'))) 
         
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
   
   