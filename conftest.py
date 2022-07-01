"""
Запуск автотестов для разных языков интерфейса
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    """Запрос типа браузера и языка веб-страниц для тестирования"""
    parser.addoption('--browser_name', action='store', default="Chrome", help='Choose browser: chrome or firefox')
    parser.addoption('--language', action='store', default='en', help="Choose language: ec or fr")

@pytest.fixture(scope="function")
def browser(request):
    """выбор браузера и языка"""
    user_language = request.config.getoption("language")
    browser_name = request.config.getoption('browser_name')

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)

    if browser_name =='chrome':
        print('\nstart chrome brouser for test..')
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    print("\nquit browser..")
    browser.quit()
    