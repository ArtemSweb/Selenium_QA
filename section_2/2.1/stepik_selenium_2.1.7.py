import time
import math 
from selenium import webdriver

driver = webdriver.Chrome()

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


driver.get("http://suninjuly.github.io/get_attribute.html")
time.sleep(1)
#считаем ответ по формуле
x_element = driver.find_element_by_id('treasure')
x = x_element.get_attribute('valuex')
y = calc(x)
"""вставляем ответ в инпут"""
input_zone = driver.find_element_by_id('answer')
input_zone.send_keys(y)

check = driver.find_element_by_id('robotCheckbox')
check_is_true = check.get_attribute('checked')
assert check_is_true is None, 'Чекбокс отмечен'
check.click()

radio = driver.find_element_by_id('robotsRule')
radio.click()

btn = driver.find_element_by_css_selector('[type="submit"]')
btn.click()

time.sleep(5)
driver.quit()
