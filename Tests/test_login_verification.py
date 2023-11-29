import locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestAccount:
    def test_login_button_log_in_to_account(self, driver):

        driver.get(locators.Locators.url_home_page)
        driver.find_element(*locators.Locators.button_sign_in_account).click()

        WebDriverWait(driver, 200).until(expected_conditions.visibility_of_element_located(locators.Locators.text_login))
        driver.find_element(*locators.Locators.field_input_email_in_window_login).send_keys('RegisteredUser@ya.ru')
        driver.find_element(*locators.Locators.field_input_password_in_window_login).send_keys('password')
        driver.find_element(*locators.Locators.button_login_in_window_login).click()
        WebDriverWait(driver, 200).until(expected_conditions.visibility_of_element_located(locators.Locators.button_place_order))

        assert driver.find_element(*locators.Locators.button_place_order).is_displayed()


    def test_login_button_personal_account(self, driver):

        driver.get(locators.Locators.url_home_page)
        driver.find_element(*locators.Locators.button_personal_account).click()

        WebDriverWait(driver, 200).until(expected_conditions.visibility_of_element_located(locators.Locators.text_login))
        driver.find_element(*locators.Locators.field_input_email_in_window_login).send_keys('RegisteredUser@ya.ru')
        driver.find_element(*locators.Locators.field_input_password_in_window_login).send_keys('password')
        driver.find_element(*locators.Locators.button_login_in_window_login).click()
        WebDriverWait(driver, 200).until(expected_conditions.visibility_of_element_located(locators.Locators.button_place_order))

        assert driver.find_element(*locators.Locators.button_place_order).is_displayed()


    def test_login_button_registration(self, driver):

        driver.get(locators.Locators.url_registration_window)
        driver.find_element(*locators.Locators.button_login_in_window_registration).click() # нажать на кнопку войти

        WebDriverWait(driver, 200).until(expected_conditions.visibility_of_element_located(locators.Locators.text_login))
        driver.find_element(*locators.Locators.field_input_email_in_window_login).send_keys('RegisteredUser@ya.ru')
        driver.find_element(*locators.Locators.field_input_password_in_window_login).send_keys('password')
        driver.find_element(*locators.Locators.button_login_in_window_login).click()
        WebDriverWait(driver, 200).until(expected_conditions.visibility_of_element_located(locators.Locators.button_place_order))

        assert driver.find_element(*locators.Locators.button_place_order).is_displayed()


    def test_login_button_password_recovery(self, driver):

        driver.get(locators.Locators.url_login_window)
        driver.find_element(*locators.Locators.button_password_recovery).click()
        driver.find_element(*locators.Locators.button_login_in_window_password_recovery).click()

        WebDriverWait(driver, 200).until(expected_conditions.visibility_of_element_located(locators.Locators.text_login))
        driver.find_element(*locators.Locators.field_input_email_in_window_login).send_keys('RegisteredUser@ya.ru')
        driver.find_element(*locators.Locators.field_input_password_in_window_login).send_keys('password')
        driver.find_element(*locators.Locators.button_login_in_window_login).click()
        WebDriverWait(driver, 200).until(expected_conditions.visibility_of_element_located(locators.Locators.button_place_order))

        assert driver.find_element(*locators.Locators.button_place_order).is_displayed()
