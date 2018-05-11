from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import apiai, json

updater = Updater(token='527735874:AAGM92qCPzon9veFzaKfUvrOLJX2j1Ggr2A')
dispatcher = updater.dispatcher


def start(bot, update):
    keyboard = [[InlineKeyboardButton(text="Исходный код", url="https://github.com/NottHell/python_bot_cko_miet"),
                 InlineKeyboardButton(text="Разработчик", url="https://vk.com/dyaleksyutenko")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Привет, давай пообщаемся?', reply_markup=reply_markup)


def message(bot, update):
    request = apiai.ApiAI('afa19533e6be4289917e2335371aa453').text_request()
    request.lang = 'ru'
    request.session_id = 'PyBot_AI'
    request.query = update.message.text
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech']
    if response:
        bot.send_message(chat_id=update.message.chat_id, text=response)
    else:
        bot.send_message(chat_id=update.message.chat_id, text='Я тебя не понял!')


start_command_handler = CommandHandler('start', start)
text_message_handler = MessageHandler(Filters.text, message)
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
updater.start_polling(clean=True)
updater.idle()

