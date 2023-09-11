from selenium import webdriver
from pages.training_ground_page import TrainingGroundPage
from pages.trial_page import TrialPage
from pages.locator import Locator


# Test Setup
browser = webdriver.Chrome()
test_value = 'it worked'


def test_trial_page():
    trial_page = TrialPage(driver=browser)
    trial_page.go()
    trial_page.stone_input.input_text('rock')
    trial_page.stone_button.click()
    assert 1 == 1;


def test_training_ground_page_button1_text():
    trng_page = TrainingGroundPage(driver=browser)
    trng_page.go()
    assert trng_page.button1.text == 'Button1'
    # trng_page.button1.click()
