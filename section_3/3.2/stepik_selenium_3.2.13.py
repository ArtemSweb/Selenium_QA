"""Задание: оформляем тесты в стиле unittest"""

from selenium import webdriver
import time
import unittest

class TestReg(unittest.TestCase):
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        inputFirstName = browser.find_element_by_css_selector('.first_block>.first_class>.first')
        inputFirstName.send_keys("Artem")

        inputSecondName = browser.find_element_by_css_selector('.first_block>.second_class>.second')
        inputSecondName.send_keys("Lantsov")

        inputEmail = browser.find_element_by_xpath('//label[contains(text(),"Email")]/following-sibling::input')
        inputEmail.send_keys("arsolodovnikov@ozon.ru")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы

        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual( "Congratulations! You have successfully registered!", welcome_text, "Кривой текст")
        #закрываем браузер
        browser.quit()

    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        inputFirstName = browser.find_element_by_css_selector('.first_block>.first_class>.first')
        inputFirstName.send_keys("Artem")

        inputSecondName = browser.find_element_by_css_selector('.first_block>.second_class>.second')
        inputSecondName.send_keys("Lantsov")

        inputEmail = browser.find_element_by_xpath('//label[contains(text(),"Email")]/following-sibling::input')
        inputEmail.send_keys("arsolodovnikov@ozon.ru")

        # Отправляем заполненную формуы
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы

        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual( "Congratulations! You have successfully registered!", welcome_text, "Кривой текст")
        # закрываем браузер после всех манипуляций
        browser.quit()

if __name__ == "__main__":
    unittest.main()