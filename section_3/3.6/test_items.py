import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_button_add_to_basket(browser):
    """Проверяем, что на странице есть кнопка добавления в корзину"""
#Запускаем браузер(само описание браузера в conftest.py)
    browser.get(link)
#можно поспать
    time.sleep(3)
#Найдем кнопку по селектору класс
    btn_add = browser.find_element_by_css_selector(".btn-add-to-basket")
#Проверим, что кнопка существует``
    assert btn_add == True, 'Кнопки не существует на странице'