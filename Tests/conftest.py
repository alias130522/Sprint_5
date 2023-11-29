import pytest
import random
import locators
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("window-size=1366,768")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    yield driver
    driver.quit()

@pytest.fixture()
def filling_registration_fields(driver, random_email):
    driver.get(locators.Locators.url_login_window)
    driver.find_element(*locators.Locators.button_registration_in_window_login).click()
    driver.find_element(*locators.Locators.field_input_name_in_registration).send_keys('admin')
    driver.find_element(*locators.Locators.field_input_email_in_registration).send_keys(random_email)
    driver.find_element(*locators.Locators.field_input_password_in_registration).send_keys('password')
    driver.find_element(*locators.Locators.button_registration_in_registration).click()
    return driver

@pytest.fixture()
def random_email():
    email = f'DmitryVolkov3{random.randint(100, 999)}@yandex.ru'
    actual_email = email
    return actual_email

@pytest.fixture()
def filling_input_fields(driver):
    driver.get(locators.Locators.url_login_window)
    WebDriverWait(driver, 200).until(expected_conditions.visibility_of_element_located(locators.Locators.text_login))
    driver.find_element(*locators.Locators.field_input_email_in_window_login).send_keys('RegisteredUser@ya.ru')
    driver.find_element(*locators.Locators.field_input_password_in_window_login).send_keys('password')
    driver.find_element(*locators.Locators.button_login_in_window_login).click()
    WebDriverWait(driver, 200).until( expected_conditions.visibility_of_element_located(locators.Locators.button_place_order))
    return driver




