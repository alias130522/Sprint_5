import locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestPersonalAccount:

    def test_click_personal_account(self, driver, filling_input_fields): # Проверка перехода по клику на «Личный кабинет».

        driver.find_element(*locators.Locators.button_personal_account).click()
        WebDriverWait(driver, 200).until(expected_conditions.visibility_of_element_located(locators.Locators.button_save_in_personal_account))
        assert driver.find_element(*locators.Locators.button_save_in_personal_account).is_displayed()

    def test_click_constructor_from_personal_account(self, driver, filling_input_fields):

        driver.find_element(*locators.Locators.button_constructor).click()
        WebDriverWait(driver, 200).until(expected_conditions.visibility_of_element_located(locators.Locators.button_place_order))
        assert driver.find_element(*locators.Locators.button_place_order).is_displayed()

    def test_click_stellar_burgers_from_personal_account(self, driver, filling_input_fields):

        driver.find_element(*locators.Locators.button_logo_stellar_burgers).click()
        WebDriverWait(driver, 200).until( expected_conditions.visibility_of_element_located(locators.Locators.button_place_order))
        assert driver.find_element(*locators.Locators.button_place_order).is_displayed()

    def test_click_button_exit_from_personal_account(self, driver, filling_input_fields):

        driver.find_element(*locators.Locators.button_personal_account).click()
        WebDriverWait(driver, 200).until(expected_conditions.visibility_of_element_located(locators.Locators.button_save_in_personal_account))
        driver.find_element(*locators.Locators.button_exit_from_personal_account).click()
        WebDriverWait(driver, 200).until(expected_conditions.visibility_of_element_located(locators.Locators.text_login))
        assert driver.find_element(*locators.Locators.text_login).is_displayed()

