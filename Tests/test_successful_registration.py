import pytest
import locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestRegistration:
    def test_successful_registration(self, driver, filling_registration_fields, random_email):

        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(locators.Locators.text_login))
        assert driver.find_element(*locators.Locators.text_login).is_displayed()

    def test_registration_with_empty_field_name(self, driver, random_email): # Проверка регистрации с незаполненым полем Имя
        driver.get(locators.Locators.url_registration_window)

        driver.find_element(*locators.Locators.field_input_email_in_registration).send_keys(random_email)
        driver.find_element(*locators.Locators.field_input_password_in_registration).send_keys('password')
        driver.find_element(*locators.Locators.button_registration_in_registration).click()
        assert driver.find_element(*locators.Locators.text_registration).is_displayed()

    @pytest.mark.parametrize('email', ['@', '', '1@', '123@', '@.'])
    def test_registration_with_invalid_data_field_email(self, driver, email):  # Проверка регистрации заполнение поля email невалидными данными
        driver.get(locators.Locators.url_registration_window)

        driver.find_element(*locators.Locators.field_input_name_in_registration).send_keys('admin')
        driver.find_element(*locators.Locators.field_input_email_in_registration).send_keys(email)
        driver.find_element(*locators.Locators.field_input_password_in_registration).send_keys('password')
        driver.find_element(*locators.Locators.button_registration_in_registration).click()
        assert driver.find_element(*locators.Locators.text_registration).is_displayed()


    @pytest.mark.parametrize('password', ['1', '123', '12345']) # Проверка регистрации заполнение поля password невалидными значениями
    def test_registration_with_invalid_data_field_password(self, driver, random_email, password):
        driver.get(locators.Locators.url_registration_window)

        driver.find_element(*locators.Locators.field_input_name_in_registration).send_keys('admin')
        driver.find_element(*locators.Locators.field_input_email_in_registration).send_keys(random_email)
        driver.find_element(*locators.Locators.field_input_password_in_registration).send_keys(password)
        driver.find_element(*locators.Locators.button_registration_in_registration).click()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(locators.Locators.text_invalid_password))
        assert driver.find_element(*locators.Locators.text_invalid_password).is_displayed()

    def test_uniqueness_field_email(self, driver, filling_registration_fields, random_email):
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(locators.Locators.text_login))
        driver.find_element(*locators.Locators.button_registration_in_window_login).click()

        driver.find_element(*locators.Locators.field_input_name_in_registration).send_keys('admin')
        driver.find_element(*locators.Locators.field_input_email_in_registration).send_keys(random_email)
        driver.find_element(*locators.Locators.field_input_password_in_registration).send_keys('password')
        driver.find_element(*locators.Locators.button_registration_in_registration).click()
        assert driver.find_element(*locators.Locators.text_user_already_exists).is_displayed()