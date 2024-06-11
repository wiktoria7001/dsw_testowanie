
Feature: User Registration

  Scenario Outline: Register a new user
    Given I sign in super APP
    When User is registered with email:<email> password:<password>
    Then Registration is successful
    And User token is not empty

    Examples:
      | email               | password |
      | eve.holt@reqres.in  | pistol   |
