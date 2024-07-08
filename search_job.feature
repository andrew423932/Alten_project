Feature: Search job field

  @scenario1
  Scenario: There is more than one jobs
     Given the client got navigated to home page
      When the client enter a valid job into the seach box field
      And the client click on seach icon
      Then valid jobs should be displayed in search results

  @scenario2
  Scenario: There is not any jobs
     Given the client got navigated to home page
      When the client enter an invalid job into the seach box field
      And the client click on seach icon
      Then zero valid jobs should be displayed in search results

  @scenario3
  Scenario: Find remote jobs
     Given the client got navigated to home page
      When the client enter TELETRABAJO into the search box field
      And the client click on seach icon
      Then valid jobs should be displayed in search results