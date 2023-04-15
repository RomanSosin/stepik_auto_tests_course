from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Считываем значения x и считаем функцию
    x_1 = browser.find_element(By.ID, "input_value").text
    y = calc(x_1)

    # Прокручиваем страницу до поля input
    input1 = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView();", input1)

    # Вводим ответ в поле input1
    input1.send_keys(y)

    # Кликаем чек бокс и выбираем радиокнопку
    checkbox1 = browser.find_element(By.ID, "robotCheckbox").click()
    time.sleep(1)

    radiobutton2 = browser.find_element(By.ID, "robotsRule").click()
    time.sleep(1)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    # успеваем скопировать код за __ секунд
    time.sleep(6)
    # закрываем браузер после всех манипуляций
    browser.quit()
