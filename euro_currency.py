#!/usr/bin/env python
# coding: utf-8

# посмотреть ошибки mail
# open /var/mail

# crontab -e
# 0 9-18 * * * /Users/molchanov/opt/anaconda3/bin/python3 /Users/molchanov/projects/parser/solid/euro_currency.py
# https://scrapfly.io/blog/scraping-using-browsers/

import os
import requests
from bs4 import BeautifulSoup

# библиотека для динамических web
from selenium import webdriver

import warnings
warnings.filterwarnings("ignore")

# через cronetab не видет путь
cwd = '/Users/molchanov/dev/solid_cur' # os.getcwd()

with open(f'{cwd}/url.txt') as f:
    main_url = f.read()

def get_bot_info(file_path):
    # Open the file in read mode
    with open(file_path, "r") as file:
        # Read the entire contents of the file
        file_contents = file.readlines()

    return [f.strip() for f in file_contents]

    
def telegram_bot_sendtext(bot_message):

    bot_info = get_bot_info(f'{cwd}/bot_info.txt')
    bot_token = bot_info[0]
    bot_chatID = bot_info[1]
    send_text = ('https://api.telegram.org/bot' + 
                bot_token + '/sendMessage?chat_id=' + 
                bot_chatID + '&parse_mode=Markdown&text=' + bot_message)

    response = requests.get(send_text)

    return response.json()

def main():
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=options) 
    driver.get(main_url)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    currency = soup.find_all('tbody', id='currency_rate_solid')

    usd = float(currency[0].text[8:13].replace(',','.'))
    eur = float(currency[0].text[-5:].replace(',','.'))

    # telegram_bot_sendtext('check')

    with open(f'{cwd}/cur_eur.txt') as f:
        cur_eur = f.read()

    if eur != float(cur_eur):

        telegram_bot_sendtext(
            f"usd: {str(usd)} \
| eur: {str(eur)} \
| {round(eur/usd, 4)}")

        with open(f'{cwd}/cur_eur.txt', 'w') as f:
            f.write(str(eur))
            
if __name__ == '__main__':
    main()