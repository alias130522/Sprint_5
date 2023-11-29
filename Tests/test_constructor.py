import locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestConstructor:
    def test_go_to_section_bulki(self, driver):
        driver.get(locators.Locators.url_home_page)
        driver.find_element(*locators.Locators.button_souses).click()
        driver.find_element(*locators.Locators.button_bulki).click()
        WebDriverWait(driver, 200).until(expected_conditions.visibility_of_element_located(locators.Locators.text_bulki))
        assert driver.find_element(*locators.Locators.text_bulki).is_displayed()

    def test_go_to_section_sauces(self, driver):
        driver.get(locators.Locators.url_home_page)
        driver.find_element(*locators.Locators.button_souses).click()
        WebDriverWait(driver, 200).until(expected_conditions.visibility_of_element_located(locators.Locators.text_souses))
        assert driver.find_element(*locators.Locators.text_souses).is_displayed()

    def test_go_to_section_nachinki(self, driver):
        driver.get(locators.Locators.url_home_page)
        driver.find_element(*locators.Locators.button_nachinki).click()
        WebDriverWait(driver, 200).until(expected_conditions.visibility_of_element_located(locators.Locators.text_nachinki))
        assert driver.find_element(*locators.Locators.text_nachinki).is_displayed()
