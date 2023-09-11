from selenium.webdriver.common.by import By
from pages.base_element import BaseElement
from pages.base_page import BasePage
from pages.locator import Locator


class TrialPage(BasePage):
    url = 'https://techstepacademy.com/trial-of-the-stones'

    @property
    def stone_input(self):
        locator = Locator(by=By.CSS_SELECTOR, value='input#r1Input')

        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def stone_button(self):
        locator = Locator(by=By.CSS_SELECTOR, value='button#r1Btn')
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def secret_input(self):
        locator = Locator(by=By.CSS_SELECTOR, value='input#r2Input')
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def secret_button(self):
        locator = Locator(by=By.CSS_SELECTOR, value='button#r2Btn')
        return BaseElement(
            driver=self.driver,
            locator=locator
        )
