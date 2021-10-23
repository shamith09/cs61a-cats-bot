import time
from splinter import Browser
from PIL import Image
import requests
import urllib

import easyocr
reader = easyocr.Reader(['en'])

executable_path = {'executable_path':'C:/Users/shami/Downloads/chromedriver_win32/chromedriver'}

with Browser('chrome', **executable_path) as browser:
    url = 'https://cats.cs61a.org'
    browser.visit(url)
    browser.find_by_xpath('/html/body/div[3]/div/div/div[3]/button[1]').click()
    letters = browser.find_by_tag('span')
    browser.find_by_css('.InputField').click()
    text = ''
    for i in range(len(letters)):
        if i < 20:
            browser.find_by_css('.InputField').type(letters[i].value, slowly=False)
        else:
            text += letters[i].value
    browser.find_by_css('.InputField').type(text, slowly=False)
    browser.find_by_xpath('/html/body/div[3]/div/div/div[2]/div/button').click()
    """
    ANSWERS = {

    }
    """
    captcha_urls = browser.find_by_tag('img')
    for c in captcha_urls:
        urllib.request.urlretrieve(c._element.get_attribute('src'), './img')
        try:    
            txt = reader.readtext('img', detail=0)[0]
        except:
            print('error')
        browser.find_by_css('.InputField').type(txt, slowly=False)

    browser.find_by_xpath('/html/body/div[3]/div/div/div[2]/div/div[3]/button').click()
    time.sleep(60)