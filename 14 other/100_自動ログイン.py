'''
Seleniumを用いて、下記サイトに自動ログインを行ってください

- username: imanishi
- password: kohei
https://scraping-for-beginner.herokuapp.com/login_page

「pip3 install -U selenium」
「pip3 install webdriver_manager」
'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# ドライバーのクロムの環境のバージョンが違うのを避ける為の作法
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.implicitly_wait(10)  # 待機する時間設定（１０秒）

url = 'https://scraping-for-beginner.herokuapp.com/login_page'
browser.get(url)
elem_username = browser.find_element(By.ID, 'username')
elem_username.send_keys('imanishi')
elem_password = browser.find_element(By.ID, 'password')
elem_password.send_keys('kohei')
login_btn = browser.find_element(By.ID, 'login-btn')
login_btn.click()

time.sleep(3)
browser.quit()

