class BasePage(object):

    url = None

    def __init__(self, driver, url=None):
        self.driver = driver

    def go(self):
        self.driver.get(self.url)
        