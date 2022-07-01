"""
Запуск автотестов для разных языков интерфейса
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    """Запрос языка веб-страниц для тестирования"""
    parser.addoption('--language', action='store', default='en', help="Choose language: ec or fr")

@pytest.fixture(scope="function")
def browser(request):
    """выбор браузера и языка"""
    user_language = request.config.getoption("language")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)

    yield browser
    print("\nquit browser..")
    browser.quit()
    