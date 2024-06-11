Feature: Login

  Scenario Outline: User login
    Given I log in super APP
    When User logs in with email:<email> password:<password>
    Then User is successfully logged in
    And Login token is returned

    Examples:
      | email              | password |
      | eve.holt@reqres.in | pistol   |
