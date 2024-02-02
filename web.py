import requests
import tracemalloc
from bs4 import BeautifulSoup
from telegram import Bot
import logging
import time

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def scraping_data():
    url = 'https://www.ethiopianreporter.com/'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        titles = soup.find_all('h2', class_='post-title')
        news_data = [title.text.strip() for title in titles]
        return '\n'.join(news_data)
    else:
        logging.error("Failed to fetch data from the website.")
        return "Failed to fetch data from the website."

def send_to_telegram_bot(bot_token, chat_id, data):
    bot = Bot(token=bot_token)
    try:
        bot.send_message(chat_id=chat_id, text=data)
        logging.info("Sent data to Telegram bot.")
    except Exception as e:
        logging.error(f"Failed to send data to Telegram bot: {e}")

def main():
    BOT_TOKEN = '6355817548:AAENxu8o-wthbjL-ZP9vVMFOfNDh7IqyaME'
    BOT_CHAT_ID = '788123983'
    
    while True:
        data = scraping_data()
        try:
            send_to_telegram_bot(BOT_TOKEN, BOT_CHAT_ID, data)
        except Exception as e:
            logging.error(f"An error occurred after sending data to Telegram bot: {e}")
        time.sleep(3600)

if __name__ == '__main__':
    main()




    
