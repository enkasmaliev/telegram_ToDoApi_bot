import json

import telebot
from telebot import types

from main import api

token = '6275354080:AAEzIsaZofyrb-eDowBLGJ3KRRiVPiT3qyQ'

bot = telebot.TeleBot(token)

inline_keyboard = types.InlineKeyboardMarkup()
inline_button = types.InlineKeyboardButton('Create', callback_data='create')
inline_button1 = types.InlineKeyboardButton('Read', callback_data = 'read')
inline_button2 = types.InlineKeyboardButton('Retrieve', callback_data='retrieve')
inline_button3 = types.InlineKeyboardButton('Update', callback_data='update')
inline_button4 = types.InlineKeyboardButton('Delete', callback_data='delete')
inline_keyboard.add(inline_button, inline_button1, inline_button2, inline_button3, inline_button4)

def choose_action(message: types.Message):
    bot.send_message(message.chat.id, 'Выбери действие: ', reply_markup=inline_keyboard)

@bot.message_handler(commands=['start'])
def start_bot(message: types.Message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')
    choose_action(message)

@bot.callback_query_handler(func=lambda callback: callback.data == 'read')
def read_api(callback: types.CallbackQuery):
    text = json.dumps(api.read(), indent=4, ensure_ascii=False)
    bot.send_message(callback.message.chat.id, text)
    choose_action(callback.message)

@bot.callback_query_handler(func=lambda callback: callback.data == 'create')
def create_api(callback: types.CallbackQuery):
    input_ = bot.send_message(callback.message.chat.id, 'Введите title: ')
    bot.register_next_step_handler(input_, create)

def create(message: types.Message):
    response = message.text
    bot.send_message(message.chat.id, api.create(response))
    choose_action(message)
    

@bot.callback_query_handler(func=lambda callback: callback.data == 'retrieve')
def retrieve_api(callback: types.CallbackQuery):
    input_ = bot.send_message(callback.message.chat.id, 'Введите id: ')
    bot.register_next_step_handler(input_, retrieve_id)

def retrieve_id(message: types.Message):
    response = message.text
    res = json.dumps(api.retrieve(response), indent=4, ensure_ascii=False)
    bot.send_message(message.chat.id, res)
    choose_action(message)

@bot.callback_query_handler(func=lambda callback: callback.data == 'update')
def update_api(callback: types.CallbackQuery):
    input_ = bot.send_message(callback.message.chat.id, 'Введите id и новый title через пробел: ')
    bot.register_next_step_handler(input_, update)

def update(message: types.Message):
    response = message.text.split()
    bot.send_message(message.chat.id, api.update(response[0], response[1]))
    choose_action(message)

@bot.callback_query_handler(func=lambda callback: callback.data == 'delete')
def delete_api(callback: types.CallbackQuery):
    input_ = bot.send_message(callback.message.chat.id, 'Введите id: ')
    bot.register_next_step_handler(input_, delete_id)

def delete_id(message: types.Message):
    response = message.text
    bot.send_message(message.chat.id, api.delete(response))
    choose_action(message)



bot.polling()