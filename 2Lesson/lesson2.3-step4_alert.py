"""
1. Открыть страницу http://suninjuly.github.io/alert_accept.html
2. Нажать на кнопку
3. Принять confirm
4. На новой странице решить капчу для роботов, чтобы получить число с ответом
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # переключаемся на alert и подтвержаем
    confirm = browser.switch_to.alert
    confirm.accept()

    number = browser.find_element(By.ID, "input_value").text

    result = calc(number)

    browser.find_element(By.ID, "answer").send_keys(result)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    # успеваем скопировать код за __ секунд
    time.sleep(6)
    # закрываем браузер после всех манипуляций
    browser.quit()
