import telebot
import requests

BOT_TOKEN = '8309084861:AAHmzx7uyvriDDJ-BYba7mvvZjf6NhIxsXI'
API_KEY = 'b01e7608c07f15c54ff9d9b64d478705'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "shahar nomini yozing:")

@bot.message_handler(func=lambda m: True)
def obhavo(message):
    shahar = message.text
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={shahar}&appid={API_KEY}&units=metric&lang=uz"
    data = requests.get(url).json()
    
    if data.get('main'):
        harorat = data['main']['temp']
        holat = data['weather'][0]['description']
        
        javob = f"{shahar}\n {harorat}°C\n {holat}"
        bot.send_message(message.chat.id, javob)
    else:
        bot.send_message(message.chat.id, "sshahar topilmadi")

if __name__ == '__main__':
    print("Bot ishga tushid")
    bot.infinity_polling()