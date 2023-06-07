from behave import given, when, then
from selenium.webdriver.common.by import By
from auto_tests.selenium_tests.blog_test import LoginPage, HomePage, BlogPostPage


@given('I am logged in')
def step_given_i_am_logged_in(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open()
    context.login_page.login("new5_user_for_12553@gmail.com", "asdf@1234")


@given('I am on the home page')
def step_given_i_am_on_the_home_page(context):
    context.home_page = HomePage(context.driver)
    context.home_page.open()


@when('I click on the add post link')
def step_when_i_click_on_add_post_link(context):
    context.driver.save_screenshot('homepage2.png')
    context.home_page.click_add_post()


@when('I add a post with title "{title}" and content "{content}"')
def step_when_i_add_post(context, title, content):
    context.blog_post_page = BlogPostPage(context.driver)
    context.blog_post_page.add_post(title, content)


@then('I should see the blog "{message}" message')
def step_then_i_should_see_message(context, message):
    assert context.driver.find_element(By.CSS_SELECTOR, "body > header > div").text == message
