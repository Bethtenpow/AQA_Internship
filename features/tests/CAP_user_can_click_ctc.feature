# Created by elizabethtenpow at 3/19/24
Feature: Reely.oi Company Connect Test


  Scenario: User clicks on “Connect the company” button and can use the form to register a new agency

    Given Open the main home page
    When Login to page
    And Click continue button
    And Click on "Connect The Company"
    And Switch to a new window
   Then Enter test form information
    And Verify information is present
    And Verify "Send Request" button
    And Verify "Buy a Subscription" button

