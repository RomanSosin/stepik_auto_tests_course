from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Считываем значения двух чисел
    sum_1 = browser.find_element(By.ID, "num1").text
    sum_2 = browser.find_element(By.ID, "num2").text

    # # Считаем сумму
    summ = int(sum_1) + int(sum_2)
    # Инициализируем новый объект передаем в него select
    select = Select(browser.find_element(By.ID, "dropdown"))

    # Ищем в списке value = summ
    select.select_by_value(str(summ))
    time.sleep(2)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за __ секунд
    time.sleep(6)
    # закрываем браузер после всех манипуляций
    browser.quit()
