from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)

class Browser:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def navigate_to_saucelab(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()

    def close_window(self):
        self.driver.quit()
