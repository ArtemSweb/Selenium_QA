import time
import os
from selenium import webdriver

browser = webdriver.Chrome()

link = 'http://suninjuly.github.io/file_input.html'

try:
    browser.get(link)
    time.sleep(1)

    """Вставляет текст в инпут firstame"""
    fName = browser.find_element_by_tag_name('[name="firstname"]')
    fName.send_keys('Артем')

    """Вставляет текст в инпут lastname"""
    lName = browser.find_element_by_tag_name('[name="lastname"]')
    lName.send_keys('Солодовников')

    """Вставляет текст в инпут email"""
    email = browser.find_element_by_tag_name('[name="email"]')
    email.send_keys('arsolodovnikov@ozon.ru')

    """загрузить файл"""
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'for_2.2.8.txt')      # указываем, что файл в директории со скриптом
    browser.find_element_by_id('file').send_keys(file_path)     # Добавляем файл

    """клик на кнопку"""
    btn = browser.find_element_by_css_selector('[type="submit"]')
    btn.click()

finally:
    time.sleep(5)
    browser.quit()
