from flask import Flask, request
import os
from telegram import Bot, Update

TOKEN = "7714847951:AAEmSUcbjapsGeq0rVQva_qsnxzsr8mb1RM"
bot = Bot(token=TOKEN)
app = Flask(__name__)

@app.route(f"/{TOKEN}", methods=["POST"])
def respond():
    update = Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    text = update.message.text
    bot.send_message(chat_id=chat_id, text="Дякую за повідомлення! Я активний 24/7 🙂")
    return 'ok'

@app.route("/")
def index():
    return "Бот працює!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)


