import time
import math 
from selenium import webdriver

driver = webdriver.Chrome()

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


driver.get("http://suninjuly.github.io/math.html")
time.sleep(2)

x_element = driver.find_element_by_id('input_value')
x = x_element.text
y = calc(x)

input_zone = driver.find_element_by_id('answer')
input_zone.send_keys(y)

check = driver.find_element_by_css_selector('[for="robotCheckbox"]')
check.click()

radio = driver.find_element_by_css_selector('[for="robotsRule"]')
radio.click()

btn = driver.find_element_by_css_selector('[type="submit"]')
btn.click()

time.sleep(5)
driver.quit()
