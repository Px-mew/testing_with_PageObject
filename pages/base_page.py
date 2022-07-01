class BasePage():
    """Класс базовая страница, от которой будут унаследованы все остальные классы. Описаны вспомогательные методы для работы с драйвером."""
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)