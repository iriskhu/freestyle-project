import csv
import os
import json
from dotenv import load_dotenv
import requests
import pytest
import pdb



def menu(username):
    menu = f"""
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      Hello {username}, welcome to SaveMore!
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    |                       .----.          |
    |                   _.'__      `.       |
    |               .--($)($$)---  /$\      |
    |             .' @            /$$$\     |
    |             :           '  |$$$$$|    |
    |   HI         `-..__.-' _.---\$$$/     |
    |  THERE!    __      `;_:      '"'      |
    |              \   .'''''''`.           |
    |               \ /,  SAVE   ' ,        |
    |                //   MORE!   //        |
    |                `-._______.-'          |
    |                ___`. | .'___          |
    |               (______|______)         |
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     This monthly bookkeeping app will help
     you manage your budgets and expenses,
     as well as providing other related info.
     Before you start, please take a moment
     to read the description of operations
     below, thanks!
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     Description of Operations > > >
                                    v
                                    v
       < < < < < < < < < < < < < < <
      v
      v
       > >>> Record: to record your daily expenses.
         >>> Show: to show all recorded entries.
         >>> Calculate: calculate the extisting entries.
         >>> Convert: convert an amount to another currency.
         >>> Clear: clear all your records.

     Alright! Now let's get started!
     Please enter an operation: """
    return menu
    #...inspired by Inventory-mgmt-app project
    #...Spoonpy reference: http://tieba.baidu.com/p/976397192?traceid=


#def parse_response(response_text): #...inspired by Stock-app project
#    if isinstance(response_text, str): #...checking to see if the datatype of "response_text" is string---if not, then:
#        response_text = json.loads(response_text) #...converting the string to a dictionary.
#pdb.set_trace()


def read_entries_from_file(filename = "entries.csv"):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    #print(f"READING PRODUCTS FROM FILE: '{filepath}'")
    entries = []
    with open(filepath, "r") as csv_file:
        reader = csv.DictReader(csv_file) #...to assume the CSV has headers
        for ordered_dict in reader:
            entries.append(dict(ordered_dict))
    return entries


def write_entries_to_file(filename="entries.csv", entries=[]):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    print ("Writing to", filepath)
    with open(filepath, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["year", "month", "day", "category", "expense"])
        writer.writeheader()
        for entry in entries:
            writer.writerow({"year": entry["year"], "month": entry["month"], "day": entry["day"], "category": entry["category"], "expense": entry["expense"]})


def clear_entries_file(filename="entries.csv", from_filename="entries_default.csv"):
    print("CLEARING ENTRIES>>>")
    print("OK! YOUR ENTRIES HAVE BEEN CLEARED.")
    print("TIME TO START A NEW MONTHLY RECORD!")
    print("------------------------------------")
    entries = read_entries_from_file(from_filename)
    write_entries_to_file(filename, entries)
    quit()



def run(): #...to specify which function is going wrong---Prof.'s notes

    #...reading products from file 'entries.csv'
    entries = read_entries_from_file()

    #...capturing user input: user's name & choice of operation
    my_menu = menu(username=input("Hi, what's your name? "))
    operation = input(my_menu)
    print("------------------")
    print("Thanks! You've chosen: " + operation)
    print("------------------")

    operation = operation.title()


    if operation == "Record":
        entry_year = input ("Please enter the year (4 digits, e.g: 2016): " )
        entry_month = input ("Please enter the month (2 digits, e.g: 04): " )
        entry_day = input ("Please enter the day (2 digits, e.g: 01): ")
        entry_category = input ("Please enter the category (e.g: snacks): ")
        entry_expense = input ("Please enter the amount you paid: ")

        new_entry = {
            "year": entry_year,
            "month": entry_month,
            "day": entry_day,
            "category": entry_category,
            "expense": entry_expense
        }
        entries.append(new_entry)
        print("------------------")
        print(new_entry["year"] + "-" + new_entry["month"] + "-" + new_entry["day"] + ", " + new_entry["category"] + ": $" + new_entry["expense"])
        print("------------------")
        print("Congrats! You just recoreded a new entry! Keep it up!")


    elif operation == "Show":
        choice = input("Please choose 'C' to view where your money was spent, or 'A' to view all your entries: ")
        choice = choice.title()

        if choice == "A":
            print("------------------")
            print("Here are your entries so far:")
            for entry in entries:
                print(">>> " + entry["day"] + "," + entry["category"] + ": $" + entry["expense"])
            print("------------------")

        elif choice == "C": #...todo: provide a chart of catogories
            categories = []
            for entry in entries:
                categories.append(entry["category"])

            categories = set(categories)
            categories = list(categories)

            print("------------------")
            print(">>> So far your money has been spent on: " + str(categories))
            print("------------------")

        else:
            print("------------------")
            print("Oops, please try again. Please type 'A' or 'C'.")
            print("------------------")


    elif operation == "Calculate":
        monthly_budget = input("Please enter your monthly budget: ")
        print("------------------")

        sum = 0  #...reference: https://stackoverflow.com/questions/4362586/sum-a-list-of-numbers-in-python
        for entry in entries:
            int_entry = int(entry["expense"])
            sum += int_entry

        residual = int(monthly_budget) - sum
        if residual > 0:
            print("Looks good! You have spent $" + str(sum) + " so far this month---$" + str(residual) + " away from your monthly budget! Yay!")
            print("------------------")
        else:
            print("Oops, you've spent $" + str(sum) + " so far this month---more than your monthly budget. Try spending less next month!")
            print("------------------")


    elif operation == "Convert":
        load_dotenv()

        access_key = os.environ.get("CURRENCY_API_KEY") or "OOPS. Please set an environment variable named 'CURRENCY_API_KEY'."
        #print(access_key)  #...for testing purpose
        currency_code = input ("Please enter the code of a currency you want to convert to (e.g: CNY): ")

        if len(currency_code)>3:
            print("Oops! Please try again. Expecting a currency code with 3 digits.")
        else:
            try: ## try function allows us to handle errors---Prof.'s notes
                float(currency_code)
                quit("Oops! Please try again. Expecting a non-numeric currency code.")
            except ValueError as e:
                request_url = f"https://v3.exchangerate-api.com/pair/{access_key}/USD/{currency_code}"
                response = requests.get(request_url)
                #print(response.text)  #...for testing purpose

                if "error" in response.text: #...used pdb.set_trace() to test out "error" in response.text
                    print(" >.< OH NO! Your currency code cannot be found. Please Try again.")
                    quit()
                else:
                    data = response.json()  #...the website providing the api key suggests the variable 'data'. Reference: https://www.exchangerate-api.com/python-currency-api
                    print("The current exchange rate you are requesting is: " + str(data["rate"]))
                    print("------------------")


    elif operation == "Clear":
        print("------------------------")
        clear_entries_file()


    else:
        print("------------------")
        print("Oops, unrecognized operation, please try again.")
        print("----------------------")

    write_entries_to_file(entries=entries)


if __name__ == "__main__":
    run()
