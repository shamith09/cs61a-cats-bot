# CS 61A Cats Bot

Splinter bot that attempts to get on the leaderboard on cats.cs61a.org. Max typing speed was 2000+ wpm, but had to reduce it to ~450 wpm because CATS doesn't allow unrealistic typing speeds on the leaderboard (even though the world record is 216 wpm).

Currently the bot is stopped by the captcha, so I tried to get around it using OCR. However, OCR doesn't seem to be very good at solving captchas, so I will have to find another way to bypass it.

## How to use:

Install splinter using pip:

`pip install splinter`

Follow instructions on https://splinter.readthedocs.io/en/latest/drivers/chrome.html to set up the Chrome driver

Run cats_bot.py:

`py cats_bot.py`
