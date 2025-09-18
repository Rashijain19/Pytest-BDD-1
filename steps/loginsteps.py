import time
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



@given(u'launch chrome browser')
def launchBrowser(context):
    # chrome_options = Options()
    # chrome_options.add_argument("--start-maximized")
    # context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    context.driver = webdriver.Chrome()


@when(u'open orange hrm homepage')
def openHomepage(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    time.sleep(5)


@when(u'enter the username "{username}"  and "{password}"')
def loginCredentials(context, username, password):
    context.driver.find_element(By.CSS_SELECTOR, 'input[name="username"]').send_keys(username)
    context.driver.find_element(By.CSS_SELECTOR, 'input[type="password"]').send_keys(password)


@when(u'click on login button')
def loginButton(context):
    context.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()


@then(u'user lands on OrangeHRM dashboard page')
def verifyDashboard(context):
    #context.driver.wait_for_element_is_displayed(By.CSS_SELECTOR, 'header[class="oxd-topbar"] .oxd-text')
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div>p[class="oxd-text oxd-text--p orangehrm-attendance-card-state"]')))

