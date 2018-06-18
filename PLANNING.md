# Project Planning: Bookkeeping App for International Students

## Problem Statement

### Primary User

International students in the U.S., including myself.

### User Needs Statement 

As a student, I don’t have many opportunities to make money. As an international student, I have to pay a very high tuition fee, which is mostly provided by my family. Besides, the living expense is very high in many U.S. cities, especially places like NYC, SF bay area, etc. According to my own experience as well as my observation upon peers and friends, many international students like to set a monthly or daily budget, and to keep records of where their money is spent, in order to manage and save money. As a result, a simple application that allows international students to record their expense (and income, if any), set their monthly budget reminder, and convert their spending to the currency of their own country as a reference, would be of great use for them.

### As-is Process Description

1.	write down daily expenses on paper and manually calculate the sum; or put expense entries in an Excel spreadsheet and use Excel functions to calculate the sum
2.	Compare the sum of the expense with the daily budget
3.	Search online to check the updated exchange rate between USD and a specific currency
4.	Use an online converter to get the corresponding amount in the mentioned currency

### To-be Process Description

1.	Run a script to provide a menu of functions including budget setting, daily expense recording, daily total expense calculating, and currency converting.
2.	The hourly updated exchange rate will be requested via API from https://currencylayer.com/
3.	The app will provide financial suggestion according to the user’s daily total expenses and their daily budget
4.	A fun, creative user interface will attract the users to keep recording their daily expenses, which helps them to better manage their money.

## Information Requirements

### Information Inputs

1.	User’s daily expenses entries; user’s monthly budget
2.	A `get` request to obtain exchange rate data from third-party website.
  
### Information Outputs

1.	User’s daily total expenses.
2.	User’s daily budget
3.	The corresponding amount of user’s daily expenses in their home country’s currency

## Technology Requirements

### APIs and Web Service Requirements

1.	[CurrencyLayer API](https://currencylayer.com/product): free plan, which allows 1,000 request per month and provides hourly updated data.

### Python Package Requirements

1.	`os` 
2.	`csv`
3.	`pytest` (for testing purpose)

### Hardware Requirements
1.	This application will be only for private use.

### Additional Notes: This plan is subject to potential further improvements...

