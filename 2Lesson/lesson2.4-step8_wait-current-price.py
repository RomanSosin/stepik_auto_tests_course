from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser: WebDriver = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    # Ждем с помощью WebDriverWait и Expect Conditions пока сумма в поле Price будет 100 и жмем кнопку "Book"
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # Скроллим страницу до второй кнопки
    button2 = browser.find_element(By.CSS_SELECTOR, "form button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(false);", button2)

    # считаем по формуле и вводим ответ в поле "answer"
    number = browser.find_element(By.ID, "input_value").text
    result = calc(number)
    browser.find_element(By.ID, "answer").send_keys(result)
    button2.click()

finally:
    # успеваем скопировать код за __ секунд
    time.sleep(6)
    # закрываем браузер после всех манипуляций
    browser.quit()
