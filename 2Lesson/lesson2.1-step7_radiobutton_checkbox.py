import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Считываем значение X
    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    time.sleep(1)

    checkbox1 = browser.find_element(By.ID, "robotCheckbox")
    checkbox1.click()
    time.sleep(1)

    radiobutton2 = browser.find_element(By.ID, "robotsRule")
    radiobutton2.click()
    time.sleep(1)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    # успеваем скопировать код за __ секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
