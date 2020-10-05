"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import time

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn', 
        'password': 'python'
    }
}


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)
 
def planet_func(bot, update):
    planet_dict = {'Mercury': ephem.Mercury,
                       'Venus': ephem.Venus,
                         'Mars': ephem.Mars, 
                   'Jupiter': ephem.Jupiter,
                     'Saturn': ephem.Saturn,
                     'Uranus': ephem.Uranus,
                   'Neptune': ephem.Neptune,
                       'Pluto': ephem.Pluto,
                   }
    user_planet = update.message.text.split()[1] 
    print(user_planet)
    if user_planet in planet_dict:
        constellation = ephem.constellation(planet_dict[user_planet](update.message['date'])) 
        update.message.reply_text(constellation)
    else:
        
        update.message.reply_text('Напиши планету')
def main():
    mybot = Updater(settings.TOKEN, request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_func))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()
