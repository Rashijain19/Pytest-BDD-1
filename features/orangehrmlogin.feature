Feature: OrangeHRM Logo

  Background: Common steps
    Given launch chrome browser
    When open orange hrm homepage

  Scenario Outline: verify username and password and redirection to login page
    When enter the username "<username>"  and "<password>"
    When click on login button
    Then user lands on OrangeHRM dashboard page


    Examples:
      | username | password |
      | Admin    | admin123 |
      | Admin    | admin    |