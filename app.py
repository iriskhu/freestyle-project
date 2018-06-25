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
    |               .--(#)(##)---  /#\      |
    |             .' @            /###\     |
    |             :           '  |#####|    |
    |   HI         `-..__.-' _.---\###/     |
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
         >>> Update: to edit an existing entry.
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
        writer = csv.DictWriter(csv_file, fieldnames=["year", "month", "day", "category", "expenses"])
        writer.writeheader()
        for entry in entries:
            writer.writerow({"year": entry["year"], "month": entry["month"], "day": entry["day"], "category": entry["category"], "expenses": entry["expenses"]})


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
        entry_expenses = input ("Please enter the amount you paid: ")

        new_entry = {
            "year": entry_year,
            "month": entry_month,
            "day": entry_day,
            "category": entry_category,
            "expenses": "$" + entry_expenses
        }
        entries.append(new_entry)
        print("------------------")
        print(new_entry["year"] + "-" + new_entry["month"] + "-" + new_entry["day"] + ", " + new_entry["category"] + ": " + new_entry["expenses"])
        print("------------------")
        print("Congrats! You just recoreded a new entry! Keep it up!")


    elif operation == "Show":
        choice = input("Please choose 'C' to view where your money was spent, or 'A' to view all your entries: ")
        choice = choice.title()

        if choice == "A":
            print("------------------")
            print("Here are your entries so far:")
            for entry in entries:
                print(">>>" + entry["day"] + "," + entry["category"] + ": " + entry["expenses"])
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


    elif operation == "Calculate":
        monthly_budget = input("Please enter your monthly budget: ")

        print(monthly_budget)


    elif operation == "Convert":
        load_dotenv()

        access_key = os.environ.get("CURRENCY_API_KEY") or "OOPS. Please set an environment variable named 'CURRENCY_API_KEY'."
        #print(access_key)  #...for testing purpose

        request_url = f"http://www.apilayer.net/api/live?access_key=c45a7b0a95ea3e22f207f2971ae1b0fa&currencies=CNY&source=USD&format=1"
        response = requests.get(request_url)
        print(response.text)

#        currencies = parse_response(response.text)
#        print(currencies)


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
