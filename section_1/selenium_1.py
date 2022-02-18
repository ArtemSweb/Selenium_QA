# import time
# from selenium import webdriver

# driver = webdriver.Chrome()

# time.sleep(5)

# driver.get("https://stepik.org/lesson/25969/step/12")
# time.sleep(5)

# textarea = driver.find_element_by_css_selector('.textarea')

# textarea.send_keys('get()')
# time.sleep(5)

# submit_button = driver.find_element_by_css_selector('.submit-submission')

# submit_button.click()
# time.sleep(5)

# driver.quit()
# /////////////////////////////////////////
# import time
# from selenium import webdriver

# driver = webdriver.Chrome()

# time.sleep(1)

# driver.get('https://yandex.ru/')
# time.sleep(1)

# textarea = driver.find_element_by_css_selector('#text')

# textarea.send_keys('apple macbook air m1 16gb')

# submit_button = driver.find_element_by_tag_name('button')

# submit_button.click()
# /////////////////////////////////////
# from selenium import webdriver
# import time 
# import math

# link = "http://suninjuly.github.io/find_link_text"

# try:
#     browser = webdriver.Chrome()
#     browser.get(link)

#     clickLink = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
#     clickLink.click()

#     input1 = browser.find_element_by_tag_name("input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element_by_name("last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element_by_class_name("city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element_by_id("country")
#     input4.send_keys("Russia")
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()

# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# # не забываем оставить пустую строку в конце файла