from behave import given, when, then
from selenium.webdriver.common.by import By

from auto_tests.selenium_tests.blog_test import RegistrationPage


@given('I am on the registration page')
def step_given_i_am_on_the_registration_page(context):
    context.register_page = RegistrationPage(context.driver)
    context.register_page.open()


@when('I enter the username "{username}", email "{email}", and password "{password}"')
def step_when_i_enter_registration_details(context, username, email, password):
    context.driver.find_element(By.ID, "id_user_name").send_keys(username)
    context.driver.find_element(By.ID, "id_email").send_keys(email)
    context.driver.find_element(By.ID, "id_password").send_keys(password)
    context.driver.find_element(By.ID, "id_password2").send_keys(password)


@when('I click the register button')
def step_when_i_click_register_button(context):
    context.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    context.driver.save_screenshot('reg.png')


@then('I should see the registration success message')
def step_then_i_should_see_registration_success_message(context):
    message = context.driver.find_element(By.CSS_SELECTOR, ".message").text
    assert message == "Реєстрація успішна!"


@then('I should see the logout "{link_text}" link')
def step_then_i_should_see_link(context, link_text):
    elements = context.driver.find_elements(By.LINK_TEXT, link_text)
    assert len(elements) > 0
