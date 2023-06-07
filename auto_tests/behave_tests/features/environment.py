from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def before_all(context):
    chrome_options = Options()
    chrome_options.headless = True
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.implicitly_wait(10)


def after_all(context):
    context.driver.quit()
