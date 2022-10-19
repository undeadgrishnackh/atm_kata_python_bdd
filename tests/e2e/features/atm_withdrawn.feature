Feature: ATM Withdrawn

  Scenario Outline: simple withdrawn using a single type of note
    Examples:
      | amount | notes_count |
      |  500 | 1 |
      | 1000 | 2 |
      | 1500 | 3 |
      |  200 | 1 |
      |  100 | 1 |
      |    1 | 0 |
      |   40 | 2 |
  Given the ATM machine 
  When an user wants to withdrawn <amount>
  Then the ATM will provide <notes_count> notes


  Scenario Outline: complex withdrawn using a multiple type of note
    Examples:
      | amount | notes_count |
      |     30 | 2 |
      |     60 | 2 |
      |    110 | 2 |
      |   1490 | 7 |
  Given the ATM machine
  When an user wants to withdrawn <amount>
  Then the ATM will provide <notes_count> notes


  Scenario Outline: withdrawn resulting in an error
    Examples:
      | amount | notes_count |
      |  0 | -1 |
      |1501| -1 |
  Given the ATM machine
  When an user wants to withdrawn <amount>
  Then the ATM will provide <notes_count> notes


#    maybe 1499 --> 0 notes boh/dunno
  Scenario Outline: withdrawn resulting in a crazy amount
    Examples:
      | amount | notes_count |
      |  1499  | 0 |
      |    11  | 0 |
  Given the ATM machine
  When an user wants to withdrawn <amount>
  Then the ATM will provide <notes_count> notes
