from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def fill_form(self, link):
        browser = self.browser
        browser.implicitly_wait(5)
        browser.get(link)

        # заполняем обязательные поля
        browser.find_element(By.CSS_SELECTOR, 'input[required].first').send_keys("Ivan")
        browser.find_element(By.XPATH, "//div[@class = 'first_block']/div/input[contains(@class, 'second')]").send_keys("Petrov")
        browser.find_element(By.XPATH, "//div[@class = 'first_block']/div/input[contains(@class, 'third')]").send_keys("email@mail.ru")

        # отправляем заполненную форму
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        # сохраняем текст заголовка об успешной регистрации
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1").text
        return welcome_text_elt

    def test_registration1(self):
        link1 = 'http://suninjuly.github.io/registration1.html'
        registration_result = self.fill_form(link1)
        # Сравниваем ожидаемый результат с фактическим для первой формы
        self.assertEqual('Congratulations! You have successfully registered!', registration_result, "Fill in all the fields")

    def test_registration2(self):
        link2 = 'http://suninjuly.github.io/registration2.html'
        registration_result = self.fill_form(link2)
        # Сравниваем ожидаемый результат с фактическим для второй формы (тут будет ошибка)
        self.assertEqual('Congratulations! You have successfully registered!', registration_result, "Fill in all the fields")

    def tearDown(self):
        self.browser.close()

if __name__ == '__main__':
    unittest.main()
