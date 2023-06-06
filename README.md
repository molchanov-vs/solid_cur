# solid_cur

To get usd/rub and euro/rub currency from https://solid.ru/
Script sends it to your telegram-bot.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation

```
conda create --name solid_cur python=3.9
conda activate solid_cur
pip install -r requirements.txt
```

## Usage

1. Create bot_info.txt
2. Add bot_token and bot_chatID to txt file.
3. In terminal: crontab -e
4. 0 9-18 * * 1-5 /../solid_cur/bin/python3 /../solid_cur/euro_currency.py

