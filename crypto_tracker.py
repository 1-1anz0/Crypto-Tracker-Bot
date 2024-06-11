import requests
import datetime
from telebot import telebot
from auth_data import TOKEN_API
from telebot import types


def crypto_cost(crypto_name, valyuta):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={crypto_name}&vs_currencies={valyuta}'
    response = requests.get(url=url)
    data = response.json()
    current_time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")

    if crypto_name in data:
        return f"{crypto_name.capitalize()} : bahasy {data[crypto_name][valyuta]}$ sene :{current_time}"
    else:
        return 'Sorry somthing went Wrong'
    
bot = telebot.TeleBot(TOKEN_API)

@bot.message_handler(commands=['start'])
def start_btn(message):
    if message:
        klawiatura = types.InlineKeyboardMarkup(row_width=2)

        bitcoin = types.InlineKeyboardButton('Bitcoin bahasy', callback_data='bitcoin')
        litecoin = types.InlineKeyboardButton('Litecoin bahasy', callback_data='litecoin')
        ethereum = types.InlineKeyboardButton('Ethereum bahasy', callback_data='ethereum')

        klawiatura.add(bitcoin, litecoin, ethereum)

        bot.send_message(message.chat.id, 'Haysy kripto-walyutan bahasyny bilmek isleyaniz?', reply_markup=klawiatura)



crypto = ''

@bot.callback_query_handler(func= lambda call: call.data in ['usd', 'eur', 'bitcoin', 'litecoin', 'ethereum'])
def answer_when_click_btn(callback):
    if callback.message:
        global crypto
        markup = types.InlineKeyboardMarkup(row_width=2)

        dollar = types.InlineKeyboardButton('USD', callback_data='usd')
        euro = types.InlineKeyboardButton('EURO', callback_data='eur')

        markup.add(dollar, euro)


        if callback.data == 'bitcoin':
            bot.send_message(callback.message.chat.id, 'Haysy Pul birlikde bilmek isleyaniz?', reply_markup=markup)
            crypto = 'bitcoin'
        

        elif callback.data == 'litecoin':
            bot.send_message(callback.message.chat.id, 'Haysy Pul birlikde bilmek isleyaniz?', reply_markup=markup)
            crypto = 'litecoin'

        elif callback.data == 'ethereum':
            bot.send_message(callback.message.chat.id, 'Haysy Pul birlikde bilmek isleyaniz?', reply_markup=markup)
            crypto = 'ethereum'


        
        elif callback.data == 'usd':
            print(crypto)
            bot.send_message(callback.message.chat.id, crypto_cost(crypto, 'usd'))
        
        elif callback.data == 'eur':
            bot.send_message(callback.message.chat.id, crypto_cost(crypto, 'eur'))


        
        
        start_btn(callback.message)


bot.polling()
