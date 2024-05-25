import telebot 
from telebot import types

bot = telebot.TeleBot('7174051645:AAE166omajLs1NgOvF2tQhJyJlmEhyPh5GQ')
from db import Database
import db
db = Database('database.db')
import tracemalloc
tracemalloc.start()
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

keyboard = telebot.types.ReplyKeyboardMarkup(True , True)
keyboard.row("Условие\Terms📃", "Баланс/Balance😻")
keyboard.row("Кошелек\Wallet🎒", "memewChat[Ru]🇷🇺")
keyboard.row("Приглашай деловых котов😺",)


keyboard1 = telebot.types.InlineKeyboardMarkup()
button1 = telebot.types.InlineKeyboardButton(text="Подписаться😻", url="https://t.me/memewcoin")
button2 = telebot.types.InlineKeyboardButton(text="Проверить✅" , callback_data="check_subscription")
keyboard1.add(button1 )
keyboard1.add(button2)

def create_keyboard(wallet_address):
    _keyboard = telebot.types.InlineKeyboardMarkup()
    save_button = telebot.types.InlineKeyboardButton("Сохранить✅", callback_data=f"save {wallet_address}")
    cancel_button = telebot.types.InlineKeyboardButton(text="Отмена🚫", callback_data="cancel")
    _keyboard.add(save_button, cancel_button)
    return _keyboard
 


wallet_address = ""

@bot.message_handler(func=lambda message: message.text in ["Условие\Terms📃", "Баланс/Balance😻", "Кошелек\Wallet🎒", "memewChat[Ru]🇷🇺","Приглашай деловых котов😺"])
def button_click(message): 
    if message.text == "Условие\Terms📃":
        usr_id = message.chat.id
        bot.send_photo(message.chat.id, 'https://imgbly.com/ib/deJek2aUww' , caption= "Условие\Terms📃  \n Условия участия в AIRDROP не были еще такими простыми 😱 \n Абсолютно каждый участник получит токены $MEMEW \n\nЧтобы участвовать, Вам необходимо:\n 1. Быть подписанным на канал:@memewcoin \n2. Приглашай  деловых котов  для получения $MEMEW \n Вы можете пригласить деловых котов  по вашей персональной ссылке:https://t.me/memewDrop_Bot?start={}".format(usr_id))
    elif message.text == "Баланс/Balance😻":
        bot.send_photo(message.chat.id, 'https://ibb.co/b1X9jHx' , caption= f"Ваш Баланс: {db.count_referals(message.chat.id)*100} $MEMEW \n 1 cat = 100 $MEMEW \n Кол-во деловых котов😺: {db.count_referals(message.chat.id)}")
    elif message.text == "Кошелек\Wallet🎒":
        wallet_address = db.get_wallet(message.chat.id)
        bot.register_next_step_handler(bot.send_photo(message.chat.id,'https://ibb.co/4PtF2zY',caption= f"Ваш кошелек: {wallet_address} \n \n Привязать кошелек💸(Tonkeeper, MyTonWallet):"), add_wallet)
    elif message.text == "memewChat[Ru]🇷🇺":
        bot.send_photo(message.chat.id, 'https://ibb.co/c8VrDtF' , caption="Наш чат :@memewcoin")
    elif message.text=="Приглашай деловых котов😺":
        usr_id = message.chat.id
        bot.send_photo(message.chat.id ,'https://imgbly.com/ib/OWvz5bocwZ ', caption="Приглашай деловых котов  по своей персональной ссылке:\nhttps://t.me/memewDrop_Bot?start={} \n\n 1 cat😺 = 100 $MEMEW".format(usr_id))
    
    
def add_wallet(message):
    wallet_address = message.text
    if message.text == "Условие\Terms📃":   
        usr_id = message.chat.id
        bot.send_photo(message.chat.id, 'https://imgbly.com/ib/deJek2aUww' , caption= "Условие\Terms📃  \n Условия участия в AIRDROP не были еще такими простыми 😱 \n Абсолютно каждый участник получит токены $MEMEW \n\nЧтобы участвовать, Вам необходимо:\n 1. Быть подписанным на канал:@memewcoin \n2. Приглашай  деловых котов  для получения $MEMEW \n Вы можете пригласить деловых котов  по вашей персональной ссылке:https://t.me/memewDrop_Bot?start={}".format(usr_id))
    elif message.text == "Баланс/Balance😻":
        bot.send_photo(message.chat.id, 'https://ibb.co/b1X9jHx' , caption= f"Ваш Баланс: {db.count_referals(message.chat.id)*100} $MEMEW \n 1 cat = 100 $MEMEW \n Кол-во деловых котов😺: {db.count_referals(message.chat.id)}")
    elif message.text == "Кошелек\Wallet🎒":
        wallet_address = db.get_wallet(message.chat.id)
        bot.register_next_step_handler(bot.send_photo(message.chat.id,'https://ibb.co/4PtF2zY',caption= f"Ваш кошелек: {wallet_address} \n \n Привязать кошелек💸(Tonkeeper, MyTonWallet):"), add_wallet)
    elif message.text == "memewChat[Ru]🇷🇺":
        bot.send_photo(message.chat.id, 'https://ibb.co/c8VrDtF' , caption="Наш чат :@memewcoin")
    elif message.text=="Приглашай деловых котов😺":
        usr_id = message.chat.id
        bot.send_photo(message.chat.id ,'https://imgbly.com/ib/OWvz5bocwZ ', caption="Приглашай деловых котов  по своей персональной ссылке:\nhttps://t.me/memewDrop_Bot?start={} \n\n 1 cat😺 = 100 $MEMEW".format(usr_id))
    else:
        bot.send_message(message.chat.id, "Введенный кошелек: " + wallet_address + "\nСохранить?" , reply_markup=create_keyboard(wallet_address))

@bot.callback_query_handler(func=lambda call: call.data.startswith("save "))
def save_button_click(call):
    wallet_address = call.data.split(" ")[1]
    bot.send_message(call.message.chat.id, "Кошелек сохранен✅", reply_markup=keyboard)
    db.add_wallet(call.message.chat.id, wallet_address)
    start(call.message)
    

@bot.callback_query_handler(func=lambda call: call.data == "cancel")
def cancel_button_click(call):
    bot.send_message(call.message.chat.id, "Вы вернулись в главное меню😻" , reply_markup=keyboard)
    start(call.message)

TOKEN = "7174051645:AAE166omajLs1NgOvF2tQhJyJlmEhyPh5GQ"
CHANNEL_ID = "-1002071063100"

def check_sub_channel(chat_member):
    if chat_member.status != 'left':
        return True 
    else:
        return False 

@bot.message_handler(commands=['start'])
def start(message):
     user_id = message.from_user.id
     if check_sub_channel(bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)):
      bot.send_photo(message.chat.id, 'https://ibb.co/sszp5n1', caption="Добро пожаловать в наш проект MEMEW DROP!")
      bot.send_message(message.chat.id, "Выберите действие:", reply_markup=keyboard)
     else:
         bot.send_message(message.chat.id , "Для продолжения подпишитесь на наш канал !" , reply_markup=keyboard1 ) 

     if not db.user_exists(message.chat.id):
        start_command = message.text
        referrer_id = str(start_command[7:])
        if str(referrer_id) != "":
            if str(referrer_id) != str(message.chat.id):
                db.add_user(message.chat.id, referrer_id)
                try:
                    bot.send_message(referrer_id, "По вашей реферальной ссылке зарегестрировался деловой кот😺")
                except:
                    pass
            else:
                db.add_user(message.chat.id)
                bot.send_message(message.chat.id, "Нельзя регестрироваться по собственной реферальной ссылке!")
        else:
            db.add_user(message.chat.id)
        
        

@bot.callback_query_handler(func=lambda call: call.data == "check_subscription")
def check_subscription_callback(query):
    user_id = query.from_user.id
    if check_sub_channel(bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)):
        # Удаляем инлайн-кнопки после проверки подписки и запускаем команду /start
        bot.delete_message(query.message.chat.id, query.message.message_id)
        start(query.message)
        
    else:   
        bot.answer_callback_query(query.id, text="Вы не подписаны на канал.")
       
bot.polling()