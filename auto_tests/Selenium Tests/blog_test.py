import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class BasePage:
    def __init__(self, driver):
        self.driver = driver


class LoginPage(BasePage):
    def open(self):
        self.driver.get("http://127.0.0.1:8000/account/login/")
        self.driver.set_window_size(1000, 1000)

    def login(self, username, password):
        self.driver.find_element(By.ID, "login-username").send_keys(username)
        self.driver.find_element(By.ID, "login-pwd").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()


class RegistrationPage(BasePage):
    def open(self):
        self.driver.get("http://127.0.0.1:8000/account/register/")
        self.driver.set_window_size(1000, 1000)

    def register(self, username, email, password):
        self.driver.find_element(By.ID, "id_user_name").send_keys(username)
        self.driver.find_element(By.ID, "id_email").send_keys(email)
        self.driver.find_element(By.ID, "id_password").send_keys(password)
        self.driver.find_element(By.ID, "id_password2").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()


class HomePage(BasePage):
    def open(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.set_window_size(1000, 1000)

    def click_profile(self):
        self.driver.find_element(By.CSS_SELECTOR, ".bi-person").click()

    def click_add_post(self):
        self.driver.find_element(By.ID, "add-post").click()

    def click_logout(self):
        self.driver.find_element(By.CSS_SELECTOR, ".bi-door-closed").click()


class ProfilePage(BasePage):
    def edit_profile(self, firstname, lastname, age, website, gender):
        self.driver.find_element(By.CSS_SELECTOR, ".col-12").click()
        self.driver.find_element(By.ID, "firstname").clear()
        self.driver.find_element(By.ID, "firstname").send_keys(firstname)
        self.driver.find_element(By.ID, "lastname").clear()
        self.driver.find_element(By.ID, "lastname").send_keys(lastname)
        self.driver.find_element(By.ID, "age").clear()
        self.driver.find_element(By.ID, "age").send_keys(age)
        self.driver.find_element(By.ID, "website").clear()
        self.driver.find_element(By.ID, "website").send_keys(website)
        dropdown = self.driver.find_element(By.ID, "gender")
        dropdown.find_element(By.XPATH, f"//option[. = '{gender}']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()


class BlogPostPage(BasePage):
    def add_post(self, title, content):
        self.driver.find_element(By.ID, "title").send_keys(title)
        self.driver.find_element(By.NAME, "content").send_keys(content)
        self.driver.find_element(By.ID, "add-post").click()


class CommentPage(BasePage):
    def add_comment(self, content):
        self.driver.find_element(By.ID, "id_content").send_keys(content)
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary:nth-child(3)").click()


@pytest.fixture(scope="class")
def driver_init(request):
    chrome_options = Options()
    chrome_options.headless = True
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.mark.usefixtures("driver_init")
class TestDefaultSuite:
    @staticmethod
    def take_screenshot(driver, name):
        directory = "screenshots"
        if not os.path.exists(directory):
            os.makedirs(directory)
        driver.save_screenshot(os.path.join(directory, f"{name}.png"))

    def test_successfulRegistration(self):
        registration_page = RegistrationPage(self.driver)
        registration_page.open()
        registration_page.register(
            "new_user_for_testing12553", "new_user_for_testing12553@gmail.com", "asdf@1234"
        )
        message = self.driver.find_element(By.CSS_SELECTOR, ".message").text
        assert message == "Реєстрація успішна!"
        elements = self.driver.find_elements(By.LINK_TEXT, "Вийти")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".btn:nth-child(4)")
        assert len(elements) > 0
        self.take_screenshot(self.driver, "successful_registration")


    def test_successfulLogin(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.login("new_user_for_testing12553@gmail.com", "asdf@1234")
        elements = self.driver.find_elements(By.LINK_TEXT, "Вийти")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".btn:nth-child(4)")
        assert len(elements) > 0
        self.take_screenshot(self.driver, "successful_login")


    def test_viewProfile(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.login("new_user_for_testing12553@gmail.com", "asdf@1234")

        home_page = HomePage(self.driver)
        home_page.open()
        home_page.click_profile()
        assert self.driver.title == "My Profile"
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".btn:nth-child(4)")
        assert len(elements) > 0
        self.take_screenshot(self.driver, "view_profile")


    def test_successfulLandOnAddBlogPost(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.login("new_user_for_testing12553@gmail.com", "asdf@1234")

        home_page = HomePage(self.driver)
        home_page.open()
        home_page.click_add_post()
        assert self.driver.title == "Add New Post"
        self.take_screenshot(self.driver, "successful_landOnPost")


    def test_successfulAddBlogPost(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.login("new_user_for_testing12553@gmail.com", "asdf@1234")

        home_page = HomePage(self.driver)
        home_page.open()
        home_page.click_add_post()

        blog_post_page = BlogPostPage(self.driver)
        blog_post_page.add_post("Some neqr title", "Some neqr body")

        message = self.driver.find_element(By.CSS_SELECTOR, ".message").text
        assert message == "Blog Post posted successfully!"
        self.take_screenshot(self.driver, "successful_addPost")


    def test_successfulAddComment(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.login("new_user_for_testing12553@gmail.com", "asdf@1234")

        home_page = HomePage(self.driver)
        home_page.open()
        self.driver.find_element(By.LINK_TEXT, "Some neqr title").click()

        comment_page = CommentPage(self.driver)
        comment_page.add_comment("asdf")

        message = self.driver.find_element(By.CSS_SELECTOR, ".message").text
        assert message == "Коментар додано успішно!"
        assert self.driver.find_element(By.CSS_SELECTOR, ".col-md-9").text == "asdf"
        self.take_screenshot(self.driver, "successful_addComment")

    def test_editProfile(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.login("new_user_for_testing12553@gmail.com", "asdf@1234")

        home_page = HomePage(self.driver)
        home_page.open()
        home_page.click_profile()

        profile_page = ProfilePage(self.driver)
        profile_page.edit_profile("ashis", "raj", "25", "https://example.com", "Чоловік")

        message = self.driver.find_element(By.CSS_SELECTOR, ".message").text
        assert message == "Profile updated successfully!"
        self.take_screenshot(self.driver, "successful_editProfile")

    def test_successfulLogout(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.login("new_user_for_testing12553@gmail.com", "asdf@1234")

        home_page = HomePage(self.driver)
        home_page.open()
        home_page.click_logout()

        assert (
            self.driver.find_element(By.CSS_SELECTOR, ".account-form > .mb-4").text
            == "Вхід"
        )
        assert (
            self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").text == "Увійти"
        )
        self.take_screenshot(self.driver, "successful_logout")

