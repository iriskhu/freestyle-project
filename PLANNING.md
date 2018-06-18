# Project Planning: Bookkeeping App for International Students

## Problem Statement

### Primary User

Myself, an international students in the U.S.

### User Needs Statement 

As a student, I don’t have many opportunities to make money. As an international student, I have to pay a very high tuition fee, which is mostly provided by my family. Besides, the living expense is very high in many U.S. cities, especially places like NYC, SF bay area, etc. To get a better sense of where my money is spent, I'm used to set a monthly budget, and to keep records of all my expenses. I also like to check the exchange rate between USD and my home country currency regularly, and convert my total monthly expense to the latter. As a result, I figure that a simple application that allows me to record my expenses (and income, if any), set a monthly budget reminder, and easily check the updated exchange rate, would be of great use for myself, and/or any international students living in the U.S.

### As-is Process Description

1.	Set a monthly budget. Write down daily expenses on paper and manually calculate the total; or put expenses in an Excel spreadsheet and use Excel functions to calculate the total
2.	Compare the daily total expenses with the daily budget (calculated from the monthly budget)
3.	Search online to check the updated exchange rate between USD and home country currency every month
4.	Use an online converter to calculate the corresponding amount of monthly expenses in home country currency

### To-be Process Description

1.	Run a script to provide a menu of functions including budget setting, daily expense recording, and daily total expense calculating
2.	Use the script to request the hourly updated exchange rate via API from https://currencylayer.com/
3.	The app will provide financial suggestion according to the user’s daily total expenses and their daily budget
4.	A fun, creative user interface will attract the users to keep recording their daily expenses, which helps them to better manage their money.

## Information Requirements

### Information Inputs

1.	User’s daily expenses entries; user’s monthly budget; user's home country currency abbreviation
2.	A `request` request to obtain exchange rate data from third-party website
  
### Information Outputs

1.	User’s daily total expenses.
2.	User’s daily budget
3.	User's home country currency exchange rate in terms of USD, and the corresponding amount of user’s daily expenses in the said currency

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

