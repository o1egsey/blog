Feature: Blog Post
  Scenario: Add Blog Post
    Given I am logged in
    And I am on the home page
    When I click on the add post link
    And I add a post with title "Some o1 title" and content "Some o1 body"
    Then I should see the blog "Blog Post posted successfully!" message

  # Add more scenarios as needed
