Feature: Registration
  Scenario: User Registration
    Given I am on the registration page
    When I enter the username "JohnDoee1", email "johndoee1@example.com", and password "asdf@1234"
    And I click the register button
    Then I should see the registration success message
    And I should see the logout "Вийти" link
