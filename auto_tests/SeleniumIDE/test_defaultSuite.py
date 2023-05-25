# Generated by Selenium IDE
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


class TestDefaultSuite():
    def setup_method(self, method):
        options = Options()
        options.headless = True
        self.driver = webdriver.Chrome(chrome_options=options)

    def teardown_method(self, method):
        self.driver.quit()

    @pytest.fixture
    def auth_user(self):
        self.driver.get("http://127.0.0.1:8000/account/login/")
        self.driver.set_window_size(982, 823)
        self.driver.find_element(By.CSS_SELECTOR, ".account-form").click()
        self.driver.find_element(By.ID, "login-username").send_keys(
            "a1aasdvfff.asdd12faa34sa3sd@example.com"
        )
        self.driver.find_element(By.ID, "login-pwd").send_keys("asdf@1234")
        self.driver.find_element(By.CSS_SELECTOR, ".login").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()

        yield self.driver

    def test_successfulRegistration(self):
        self.driver.get("http://127.0.0.1:8000/account/register/")

        self.driver.set_window_size(982, 823)
        self.driver.find_element(By.ID, "id_user_name").click()
        self.driver.find_element(By.ID, "id_user_name").send_keys("asddf.a11sassdff334aaaa")
        self.driver.find_element(By.ID, "id_email").click()
        self.driver.find_element(By.ID, "id_email").send_keys(
            "a1aasdvfff.asdd12faa34sa3sd@example.com"
        )
        self.driver.find_element(By.ID, "id_password").click()
        self.driver.find_element(By.ID, "id_password").send_keys("asdf@1234")
        self.driver.find_element(By.ID, "id_password2").click()
        self.driver.find_element(By.ID, "id_password2").send_keys("asdf@1234")
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        assert (
            self.driver.find_element(By.CSS_SELECTOR, ".message").text
            == "Реєстрація успішна!"
        )
        elements = self.driver.find_elements(By.LINK_TEXT, "Вийти")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".btn:nth-child(4)")
        assert len(elements) > 0

    def test_successfulLogin(self):
        self.driver.get("http://127.0.0.1:8000/account/login/")
        self.driver.set_window_size(982, 823)
        self.driver.find_element(By.CSS_SELECTOR, ".account-form").click()
        self.driver.find_element(By.ID, "login-username").send_keys(
            "a1aasdvfff.asdd12faa34sa3sd@example.com"
        )
        self.driver.find_element(By.ID, "login-pwd").send_keys("asdf@1234")
        self.driver.find_element(By.CSS_SELECTOR, ".login").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        elements = self.driver.find_elements(By.LINK_TEXT, "Вийти")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".btn:nth-child(4)")
        assert len(elements) > 0

    def test_viewProfile(self, auth_user):
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.set_window_size(982, 823)
        self.driver.find_element(By.CSS_SELECTOR, ".bi-person").click()
        assert self.driver.title == "My Profile"
        # self.driver.find_element(By.CSS_SELECTOR, ".login").click()
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".btn:nth-child(4)")
        assert len(elements) > 0

    def test_successfulLandOnAddBlogPost(self, auth_user):
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.set_window_size(982, 823)
        self.driver.find_element(By.ID, "add-post").click()
        assert self.driver.title == "Add New Post"

    def test_successfulAddBlogPost(self, auth_user):
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.set_window_size(982, 823)
        self.driver.find_element(By.ID, "add-post").click()
        self.driver.find_element(By.ID, "title").click()
        self.driver.find_element(By.ID, "title").send_keys("Some neqr title")
        self.driver.find_element(By.NAME, "content").click()
        self.driver.find_element(By.NAME, "content").send_keys("Some neqr body")
        self.driver.find_element(By.ID, "add-post").click()
        assert (
            self.driver.find_element(By.CSS_SELECTOR, ".message").text
            == "Blog Post posted successfully!"
        )

    def test_successfulAddComment(self, auth_user):
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.set_window_size(982, 823)
        self.driver.find_element(By.LINK_TEXT, "Some neqr title").click()
        assert self.driver.title == "Post Detail Page"
        self.driver.find_element(By.ID, "id_content").click()
        self.driver.find_element(By.ID, "id_content").send_keys("asdf")
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary:nth-child(3)").click()
        assert (
            self.driver.find_element(By.CSS_SELECTOR, ".message").text
            == "Коментар додано успішно!"
        )
        assert self.driver.find_element(By.CSS_SELECTOR, ".col-md-9").text == "asdf"

    def test_ediProfile(self, auth_user):
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.set_window_size(982, 823)
        self.driver.find_element(By.CSS_SELECTOR, ".bi-person").click()
        self.driver.find_element(By.CSS_SELECTOR, ".col-12").click()
        self.driver.find_element(By.ID, "firstname").clear()
        self.driver.find_element(By.ID, "firstname").send_keys("ashis")
        self.driver.find_element(By.CSS_SELECTOR, ".login").click()
        self.driver.find_element(By.ID, "lastname").clear()
        self.driver.find_element(By.ID, "lastname").send_keys("raj")
        self.driver.find_element(By.ID, "age").clear()
        self.driver.find_element(By.ID, "age").send_keys("25")
        self.driver.find_element(By.ID, "website").clear()
        self.driver.find_element(By.ID, "website").send_keys("https://example.com")
        self.driver.find_element(By.ID, "gender").click()
        dropdown = self.driver.find_element(By.ID, "gender")
        dropdown.find_element(By.XPATH, "//option[. = 'Чоловік']").click()
        self.driver.get_screenshot_as_file("screenshot.png")
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        assert (
            self.driver.find_element(By.CSS_SELECTOR, ".message").text
            == "Profile updated successfully!"
        )

    def test_successfulLogout(self, auth_user):
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.set_window_size(982, 823)
        self.driver.find_element(By.CSS_SELECTOR, ".bi-door-closed").click()
        assert (
            self.driver.find_element(By.CSS_SELECTOR, ".account-form > .mb-4").text
            == "Вхід"
        )
        assert (
            self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").text == "Увійти"
        )
