
import telebot

API_TOKEN = "8377582564:AAHC_siZt53Z_0IkyJwaIbvc99fG8vg09U0"
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_first_name = message.from_user.first_name
    bot.reply_to(message, f"أهلاً بك يا {user_first_name}! البوت يعمل بنجاح الآن 🚀")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "أرسل أي رسالة وسيتم الرد عليك تلقائياً.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"تم استلام رسالتك: {message.text}")

print("=== البوت متصل وشغال الآن على تليجرام ===")
bot.infinity_polling()
