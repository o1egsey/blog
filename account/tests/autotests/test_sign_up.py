import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_successful_registration(self):
        # Given I navigate to the "Registration" page
        self.driver.get("http://localhost:8000/account/register/")

        # When I fill in "username" with "<username>"
        username_input = self.driver.find_element(By.NAME, "user_name")
        username_input.send_keys("asdf.aasdfff")

        # And I fill in "email" with "<email>"
        email_input = self.driver.find_element(By.NAME, "email")
        email_input.send_keys("asdf.aasdfff@example.com")

        # And I fill in "password" with "<password>"
        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys("Asdf@1234")

        # And I fill in "confirm password" with "<confirm password>"
        confirm_password_input = self.driver.find_element(By.NAME, "password2")
        confirm_password_input.send_keys("Asdf@1234")

        # And I click on the "Register Now" button
        register_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        register_button.click()

        # Then I should be successfully registered
        success_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                                 "//div[@class='alert alert-success d-flex align-items-center']")))
        self.assertTrue(success_message.is_displayed())

        # And I should land on the "Home" page
        home_page = WebDriverWait(self.driver, 10).until(EC.title_contains("Home"))
        self.assertIn("Home", self.driver.title)

        # And I should see "success" message as "Congrats! Your registration has been successful."
        self.assertEqual(success_message.text, "Реєстрація успішна!")

        # And I should see "Dashboard" and "Logout" links
        dashboard_link = self.driver.find_element(By.XPATH, "//a[contains(text(),'Dashboard')]")
        logout_link = self.driver.find_element(By.XPATH, "//a[contains(text(),'Logout')]")
        self.assertTrue(dashboard_link.is_displayed())
        self.assertTrue(logout_link.is_displayed())

    # def test_disabled_registration(self):
    #     # Given I navigate to the "Registration" page
    #     self.driver.get("http://localhost:8000/registration/")
    #
    #     # When I fill in "username" with "<username>"
    #     username_input = self.driver.find_element_by_name("username")
    #     username_input.send_keys("asdf")
    #
    #     # And I fill in "email" with "<email>"
    #     email_input = self.driver.find_element_by_name("email")
    #     email_input.send_keys("asdf.asdf@example.com")
    #
    #     # And I fill in "password" with "<password>"
    #     password_input = self.driver.find_element_by_name("password")
    #     password_input.send_keys("Asdf@1234")
    #
    #     # And I fill in "confirm password" with "<confirm password>"
    #     confirm_password_input = self.driver.find_element_by_name("confirm_password")
    #     confirm_password_input.send_keys("")
    #
    #     # And I click on the "Register Now" button

