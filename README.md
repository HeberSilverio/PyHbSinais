# **ROBÔ DE SINAIS BINANCE - TELEGRAM** 

O robô de sinais **PyHbSinais** realiza o monitoramento dos pares de criptomoedas e envia mensagens de alertas via **Telegram**. Com diversos indicadores e tempos gráficos customizavéis, é uma excelente opção para quem quer ficar por dentro das oportunidades e regiões de preços importantes.

<div align="center">
<img src = "img/botpython.png" alt="Image" height="150" width="300">
</div>

## **MANUAL DE UTILIZAÇÃO**

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

</br> 

Para capturar o **CHAT_ID**, é necessário entrar no site [https://api.telegram.org/botTOKEN/getUpdates] e substituir o **TOKEN**. Em seguida, basta enviar uma mensagem através do telegram e atualizar o site. o número do chat aparece na string: {"message_id":xxx,"from":{"id":**Número ID**.

</br> 

Pode-se alterar a criptomoeda a ser analisada substituindo-a em **TRADE_SYMBOL**, bem como seu tempo gráfico.
</br> 

<div align="center">
<img src = "https://raw.githubusercontent.com/HeberSilverio/PyHbSinais/main/img/criptotime.png">
</div>

</br> 

Os indicadores podem ser customizados e inseridos a seu critério acessando a biblioteca **Talib** no site [https://mrjbq7.github.io/ta-lib/funcs.html]. Estes indicadores podem ser configurados como na imagem abaixo:
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
Desenvolvido por Héber Silvério 👋 Fique a vontade para se conectar

<a href="https://www.linkedin.com/in/hebersilverio/" rel="nofollow"><img src="https://camo.githubusercontent.com/c93fed3759c4a34198be7edef401a101e9454245/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c696e6b6564696e2d2532333030373742352e7376673f267374796c653d666f722d7468652d6261646765266c6f676f3d6c696e6b6564696e266c6f676f436f6c6f723d7768697465266c696e6b3d68747470733a2f2f7777772e6c696e6b6564696e2e636f6d2f696e2f6d617263696c696f636f72726569612f" alt="Linkedin Badge" data-canonical-src="https://img.shields.io/badge/linkedin-%230077B5.svg?&amp;style=for-the-badge&amp;logo=linkedin&amp;logoColor=white&amp;link=https://www.linkedin.com/in/hebersilverio/" style="max-width:100%;"></a>