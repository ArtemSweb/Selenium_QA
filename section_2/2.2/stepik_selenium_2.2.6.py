import time
import math
from selenium import webdriver

browser = webdriver.Chrome()

link = 'http://suninjuly.github.io/execute_script.html'

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser.get(link)
    time.sleep(1)
    x_element = browser.find_element_by_id('input_value').text
    result = calc(x_element)

    """вставляем ответ в инпут"""
    input_zone = browser.find_element_by_id('answer')
    input_zone.send_keys(result)

    """отмечаем чекбокс"""
    check = browser.find_element_by_id('robotCheckbox')
    check_is_true = check.get_attribute('checked')
    assert check_is_true is None, 'Чекбокс отмечен'
    check.click()

    """Скрол страницы, чтоб кнопка видна стала"""
    btn = browser.find_element_by_css_selector('[type="submit"]')
    browser.execute_script('return arguments[0].scrollIntoView(true);', btn)

    """отметить радиокнопку"""
    radio = browser.find_element_by_css_selector('[for="robotsRule"]')
    radio.click()

    """клик на кнопку"""
    btn.click()

finally:
    time.sleep(5)
    browser.quit()