Feature: Card Payments Search in INTFCM
    
    Scenario Outline: Card Payments Search
    Given launch Mozilla browser
    When open INTFCM Homepage
    And Enter username "<username>" and password "<password>"
    And Click on login button
    And User must successfully login to the Dashboard page
    And Go to Issuer Fraud Management page
    And Select Detection Card Payments section
    And search card payment by "<ACC_ID>"
    And click on filter button
    #And click on next results
    And assert result by accid"<ACC_ID>"
    And click on reset button
    And search  by "<ACC_Country>"
    And click on filter button
    And click on next results
    And assert result by Acc_country"<ACC_Country>"
    And click on reset button
    And searching  by "<MCC>"
    And click on filter button
    #And click on next results
    And assert result by mcc"<MCC>"
    And click on reset button
    And search_by "<Pan_Reference>"
    And click on filter button
    And assert pan_ref result by "<Masked_Pan>"
    And click on reset button
    And searchby  "<Terminal_ID>"
    And click on filter button
    And click on next results
    And click on reset button
    And search card payment by "<ACC_ID>", "<ACC_Country>", "<MCC>", "<Pan_Reference>", "<Terminal_ID>", "<Clear_Pan>"
    And click on filter button
    And click on reset button
    And search card payment by accid&country "<ACC_ID>", "<ACC_Country>"
    And click on filter button
    #And click on next results
    And click on reset button
    And search card payment by accid&mcc "<ACC_ID>", "<MCC>"
    And click on filter button
    #And click on next results
    And click on reset button
    And search card payment by accid&panref "<ACC_ID>", "<Pan_Reference>"
    And click on filter button
    And click on reset button
    And search card payment by accid&termid "<ACC_ID>", "<Terminal_ID>"
    And click on filter button
    And click on reset button
    And search card payment by mcc&acccountry "<MCC>", "<ACC_Country>"
    And click on filter button
    And click on reset button
    And search card payment by pan "<Clear_Pan>"
    And click on filter button
    And click on reset button
    And search card payment by *pan and dates "<Clear_Pan>"
    And click on filter button
    And Error message is present or not?
    Then close the browser

Examples:
|username |	password |		ACC_ID	|		ACC_Country	|	MCC |	Pan_Reference|	Terminal_ID|	Clear_Pan|  Masked_Pan|
|A765071  |test12345|			1234567890	|		DEU  |	  	6011	|  E9C07E171704E9EAB71EF8EBDA9C4130F68514CA657CF3204C32311EE1B884A4 |00000001|4871780007053650  |487178XXXXXX3650|
