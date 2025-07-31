from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

# Using Scenario Outline in Behave Framework to pass valid and invalid credentials on Zen Portal for successful and unsuccessful login.

# User launches chrome browser
@given('the user launches Chrome browser')
def launch_browser(context):
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-popups")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")
    context.driver = webdriver.Chrome(options=options)
    context.driver.maximize_window()

# User reaches Zen Portal Homepage
@when('the user open Zen Portal Homepage')
def open_zenportal(context):
    context.driver.get("https://www.zenclass.in/login")

# User enters username and password credentials, used explicit wait 
@when('the user enters username "{username}" and password "{password}"')
def enter_credentials(context, username, password):
    # Example implementation for entering credentials
    username_input = WebDriverWait(context.driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id=':r0:']"))
    )
    password_input = WebDriverWait(context.driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id=':r1:']"))
    )
    username_input.send_keys(username)
    password_input.send_keys(password)

# User clicks on Sign in button after entering credentials
@when('the user click on Sign in button')
def click_signin(context):
    sign_in_button = WebDriverWait(context.driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    sign_in_button.click()

# User reaches the landing page upon successful login with valid credentials
# User does not reach the landing page upon invalid credentials upon unsuccessful login
# Used try and except along with if condition to check the success upon login
@then('the user must successfully login and reach the landing page')
def dashboard(context):
    try:
        context.driver.implicitly_wait(10)
        check_text = context.driver.find_element(By.XPATH,"//p[normalize-space()='Class and Tasks']").text
        
    except:
        context.driver.close()
        assert False, "Test Failed"
    if check_text == "Class and Tasks":
        assert True, "Test Passed"
    
# Checked log out functionality for Successful user, captured screenshot
@then('the user must be able to log out of Zen Portal')
def logout_zenportal(context):
    profile_button = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.ID,"profile-click-icon"))
        )
    profile_button.click()
    screenshot = context.driver.get_screenshot_as_png()
    allure.attach(screenshot, attachment_type = allure.attachment_type.PNG)
    logout_button = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[normalize-space()='Log out']"))
        )
    logout_button.click()
    context.driver.quit()
