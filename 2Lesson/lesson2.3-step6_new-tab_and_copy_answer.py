""" Открыть страницу http://suninjuly.github.io/redirect_accept.html
Нажать на кнопку
Переключиться на новую вкладку
Пройти капчу для робота и получить число-ответ """

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import pyperclip

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    browser.find_element(By.CLASS_NAME, "trollface").click()

    browser.switch_to.window(browser.window_handles[1])

    number = browser.find_element(By.ID, "input_value").text

    result = calc(number)
    browser.find_element(By.ID, "answer").send_keys(result)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    pyperclip.copy(browser.switch_to.alert.text.split(': ')[-1])

finally:
    # успеваем скопировать код за __ секунд
    time.sleep(6)
    # закрываем браузер после всех манипуляций
    browser.quit()
