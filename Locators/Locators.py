from selenium.webdriver.common.by import By

class SauceLabLocators:
    username = (By.CSS_SELECTOR, 'input.input_error[id="user-name"]')
    password = (By.CSS_SELECTOR, 'input.input_error[id="password"]')
    login_button = (By.CSS_SELECTOR, 'input.submit-button[id="login-button"]')
    title = (By.CSS_SELECTOR, 'span.title[data-test="title"]')
