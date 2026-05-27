import telebot
from flask import Flask, request

API_TOKEN = '8775629774:AAEGUY-9eiaRMaeFayqZO6jR6tUTX_r9P8w'
bot = telebot.TeleBot(API_TOKEN, threaded=False)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Calculator Bot အဆင်သင့်ဖြစ်ပါပြီ။\nဥပမာ - /cal 100+50")

@bot.message_handler(commands=['cal'])
def calculate(message):
    try:
        expr = message.text.replace('/cal', '').strip()
        result = eval(expr)
        bot.reply_to(message, f"✅ ရလဒ်: {result}")
    except:
        bot.reply_to(message, "❌ တွက်ချက်မှု မှားယွင်းနေသည်။")

@app.route('/8952691130:AAGehsa-Yv2s-iaCpjIlgUj2U-FCl1-c0D4', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "OK", 200

@app.route('/')
def index():
    return "Bot is running!"

if __name__ == "__main__":
    app.run()
