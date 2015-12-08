Feature: Registering a tester

Background:
Given I am on register page

Scenario:  Registering
    When I a register a tester
    Then I must see a success message
