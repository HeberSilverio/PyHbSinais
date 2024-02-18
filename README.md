# **ROBÔ DE SINAIS BINANCE - TELEGRAM** 

O robô de sinais **PyHbSinais** realiza o monitoramento dos pares de criptomoedas e envia mensagens de alertas via **Telegram**. Com diversos indicadores e tempos gráficos customizavéis, é uma excelente opção para quem quer ficar por dentro das oportunidades e regiões de preços importantes.

<div align="center">
<img src = "https://raw.githubusercontent.com/HeberSilverio/PyHbSinais/main/img/VisaoTelegram.JPG" alt="Image" style="max-width: 100%;">
</div>



# 📋 Índice
 
### Links úteis 
*  <a href="https://www.youtube.com/watch?v=-FHCUqYHCzY&list=PLYotAkYupgP0obtvJs3iXrNgACv9Iw1g3">Video tutorial</a> 

*  <a href="https://python-binance.readthedocs.io/en/latest/overview.html">Api da binance</a> 
*  <a href="https://github.com/TA-Lib/ta-lib-python/tree/master">Talib Python</a> 
*  <a href="https://github.com/TA-Lib/ta-lib-python/blob/master/docs/doc_index.md">Relação dos indicadores na API TA-Lib</a> 




### **MANUAL DE UTILIZAÇÃO**

Antes de começar a configurar e a utilizar, é necessário instalar a biblioteca da Binance. Digite no terminal: `pip install python-binance`

No arquivo **"config.py"** deverá ser inserida a **API_KEY** da sua conta Binance juntamente de sua senha **API_ SECRET**. Ambos podem ser obtidos nas configurações da sua conta Binance, adentrando na opção **API Management**.

<div align="center">
<img src = "https://raw.githubusercontent.com/HeberSilverio/PyHbSinais/main/img/secrets.png">
</div>


Ainda no arquivo **"config.py"**, para inserir o **TOKEN** é necessário criar um bot no Telegram utilizando o canal **BotFather**:


<div align="center">
<img src = "https://raw.githubusercontent.com/HeberSilverio/PyHbSinais/main/img/botfather.png" alt="Image" height="350" width="300">
</div>

  
Para capturar o **CHAT_ID**, basta enviar uma mensagem através do telegram ou realizar qualquer alteração no grupo.
Em seguida, utilize esta url https://api.telegram.org/botTOKEN/getUpdates e substitua o **TOKEN**. 
O número do Chat_Id aparece na string: {"message_id":xxx,"from":{"id":**Número ID**.


Pode-se alterar a criptomoeda a ser analisada substituindo-a em **TRADE_SYMBOL**, bem como seu tempo gráfico.
</br> 

<div align="center">
<img src = "https://raw.githubusercontent.com/HeberSilverio/PyHbSinais/main/img/criptotime.png">
</div>

</br> 

Os indicadores podem ser customizados e inseridos a seu critério acessando a biblioteca ![**Talib**](https://github.com/TA-Lib/ta-lib-python/blob/master/talib/_func.pxi) no site. Estes indicadores podem ser configurados como na imagem abaixo:
</br> 

<div align="center">
<img src = "https://raw.githubusercontent.com/HeberSilverio/PyHbSinais/main/img/bollingerbands.png">
</div>

</br> 

Para customizar ou adicionar uma mensagem que será enviada no Telegram, é necessário utilizar o **telegramBot.send_msg** como na imagem abaixo:
</br> 

<div align="center">
<img src = "https://raw.githubusercontent.com/HeberSilverio/PyHbSinais/main/img/msgtelegram.png">
</div>

</br> 

## Autor
Desenvolvido por **Héber Silvério** 
<a href="https://www.linkedin.com/in/hebersilverio/" rel="nofollow" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Linkedin Badge" data-canonical-src="https://img.shields.io/badge/linkedin-%230077B5.svg?&amp;style=for-the-badge&amp;logo=linkedin&amp;logoColor=white&amp;link=https://www.linkedin.com/in/hebersilverio/" style="max-width:100%;"></a>
</br>
👋 Fique a vontade para se conectar