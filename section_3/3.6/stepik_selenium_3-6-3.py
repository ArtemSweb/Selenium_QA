import pytest
import math
import time
from selenium import webdriver

def get_answer():
    return str(math.log(int(time.time())))

def get_link(num):
    return f'https://stepik.org/lesson/{num}/step/1'

list = ["236895", "236896", "236897", "236898","236899", "236903","236904", "236905"]

@pytest.mark.parametrize('url', list)   #передаем урл и список
def test_researches(url):
#Запускаем браузер для каждого нового вызова функции
    browser = webdriver.Chrome()
    try:
        browser.implicitly_wait(3)
        browser.get(get_link(url))
#ищем куда бы вставить результаты вычислений get_answer и вставляем
        browser.find_element_by_css_selector(".ember-text-area.ember-view").send_keys(get_answer())
#кликаем на кнопку проверки
        browser.find_element_by_css_selector("button.submit-submission").click()
#ищем строку с информацией о статусе вычислений
        correct = browser.find_element_by_css_selector(".smart-hints__hint")
#Проверяем корректность
        assert correct.text == "Correct!"

    finally:
        browser.quit()
