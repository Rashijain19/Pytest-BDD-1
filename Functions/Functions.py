from Locators import Locators
from pytest_bdd import when, given, parsers, then, scenario
from Setup.Browser import Browser

browser = Browser()

scenario('../Features/VerifyLoginOnSauceDemo.feature', 'VerifyLoginFeatureForUser')
# precondition
def test_successful_login():
    pass

@given('Login on SauceLab Page Open')
def navigate_to_saucelab(browser):
    browser.navigate_to_saucelab()

# When condition to perform action
@when(parsers.parse('Login with "{username}" and "{password}"'))
def login_to_saucelab(username, password):
    browser.driver.find_element(Locators.SauceLabLocators.username).send_keys(username)
    browser.driver.find_element(Locators.SauceLabLocators.password).send_keys(password)
    browser.driver.find_element(Locators.SauceLabLocators.login_button).click()

# Then condition to verify/validate the expected result
@then('User lands on Sauce Demo Product Page')
def verify_product_page():
    browser.driver.wait_for_element_displayed(Locators.SauceLabLocators.title)
