from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration2.html" #тест должен падать на этой странице, но запускаться на http://suninjuly.github.io/registration1.html
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
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# пустая строка на всякий случай