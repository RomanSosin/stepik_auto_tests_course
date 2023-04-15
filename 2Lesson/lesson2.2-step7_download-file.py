import os
import string
import random
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

s = 7  # Кол-во символов в строке
random_string = ''.join((random.choices(string.ascii_letters, k=s)))  # генерируем случайную строку
random_mail = ''.join((random.choices(string.ascii_lowercase, k=10)))  # генерируем случайную почту

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    input_First_name = browser.find_element(By.NAME, "firstname").send_keys(random_string)
    input_Last_name = browser.find_element(By.NAME, "lastname").send_keys(random_string)
    input_Email = browser.find_element(By.NAME, "email").send_keys(random_mail + '@gmail.com')

    # создаем файл в текущей директории
    try:
        Path("../../../enviroments/selenium_env/file.txt").touch(exist_ok=True)
    except:
        print('You should delete file.txt and try again')  # исключаем повторное создание файла

    button_download_file = browser.find_element(By.ID, "file")

    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, '../../../enviroments/selenium_env/file.txt')
    # загружаем файл
    button_download_file.send_keys(file_path)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(6)

    # удаляем созданный файл
    Path("../../../enviroments/selenium_env/file.txt").unlink()

    # закрываем браузер после всех манипуляций
    browser.quit()

# Еще решение с циклом
# from selenium import webdriver
# from os import path
#
# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/file_input.html")
#
# for selector, keys in {'[name = "firstname"]':"Максим", '[name = "lastname"]':"Курбанов", '[name = "email"]':"ru@ru.ru", '[id = "file"]':path.join(path.dirname(__file__), 'test.txt')}.items():
#     browser.find_element_by_css_selector(selector).send_keys(keys)
# browser.find_element_by_css_selector(".btn").click()
