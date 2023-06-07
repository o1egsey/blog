Feature: Login
  Scenario: Successful Login
    Given I am on the login page
    When I enter the username "new5_user_for_125538@gmail.com" and password "asdf@1234"
    And I click the login button
    Then I should see the "Вийти" link
    And I should see the ".btn:nth-child(4)" element
