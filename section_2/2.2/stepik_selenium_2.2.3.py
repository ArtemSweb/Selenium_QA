import time
import math
from selenium import webdriver
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()

def get_sum(a, b):
    return str(int(a) + int(b))

browser.get('http://suninjuly.github.io/selects1.html')
time.sleep(1)
first_num = browser.find_element_by_css_selector('[id="num1"]').text
second_num = browser.find_element_by_css_selector('[id="num2"]').text

value_sum = get_sum(first_num, second_num)
select = Select(browser.find_element_by_tag_name('select'))
select.select_by_visible_text(value_sum)

button = browser.find_element_by_css_selector('[type="submit"]')
button.click()

time.sleep(5)
browser.quit()