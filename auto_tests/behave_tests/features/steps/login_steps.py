from behave import given, when, then
from selenium.webdriver.common.by import By

from auto_tests.selenium_tests.blog_test import LoginPage


@given('I am on the login page')
def step_given_i_am_on_the_login_page(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open()


@when('I enter the username "{username}" and password "{password}"')
def step_when_i_enter_username_and_password(context, username, password):
    context.login_page.login(username, password)


@when('I click the login button')
def step_when_i_click_login_button(context):
    context.login_page.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()


@then('I should see the "{link_text}" link')
def step_then_i_should_see_link(context, link_text):
    link_element = context.driver.find_element(By.LINK_TEXT, link_text)
    assert link_element is not None


@then('I should see the "{element_selector}" element')
def step_then_i_should_see_element(context, element_selector):
    element = context.driver.find_element(By.CSS_SELECTOR, element_selector)
    assert element is not None


@then('I should see the "{message}" message')
def step_then_i_should_see_message(context, message):
    message_element = context.driver.find_element(By.CSS_SELECTOR, ".message").text
    assert message_element == message


@then('I should see the comment content "{content}"')
def step_then_i_should_see_comment_content(context, content):
    comment_element = context.driver.find_element(By.CSS_SELECTOR, ".col-md-9").text
    assert comment_element == content


