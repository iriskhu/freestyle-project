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
     This app will help you set your budget,
     record your expenses, calculate the total,
     and convert it to another currency. Before
     you start, please take a moment to read the
     description of operations below, thanks!
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     Description of Operations > > >
                                    v
                                    v
       < < < < < < < < < < < < < < <
      v
      v
       > >>> Budget: to set a monthly budget.
         >>> Record: to record your daily expenses.
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


def parse_response(response_text): #...inspired by Stock-app project
    if isinstance(response_text, str): #...checking to see if the datatype of "response_text" is string---if not, then:
        response_text = json.loads(response_text) #...converting the string to a dictionary.

#pdb.set_trace()


def write_entries_to_file(filename="entries.csv", entries=[]):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    print ("Writing to", filepath)
    with open(filepath, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["year", "month", "day", "category", "expenses"])
        writer.writeheader()
        for entry in entries:
            writer.writerow({"year": entry["year"], "month": entry["month"], "day": entry["day"], "category": entry["category"], "expenses": entry["expenses"]})


def read_entries_from_file(filename = "entries.csv"):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    #print(f"READING PRODUCTS FROM FILE: '{filepath}'")
    entries = []
    with open(filepath, "r") as csv_file:
        reader = csv.DictReader(csv_file) #...to assume the CSV has headers
        for ordered_dict in reader:
            entries.append(dict(ordered_dict)) #...append.() function: adding stuff to the row
    return entries


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

    #...capturing
    my_menu = menu(username=input(">>> Hi, what's your name? "))
    operation = input(my_menu)
    print("Thanks! You've chosen: " + operation)

    operation = operation.title()


    if operation == "Record":
        print("------------------")
        entry_year = input ("What year? " )
        entry_month = input ("What month? " )
        entry_day = input ("What day? ")
        entry_category = input ("What category? ")
        entry_expenses = input ("How much did you spend? ")

        new_entry = {
            "year": entry_year,
            "month": entry_month,
            "day": entry_day,
            "category": entry_category,
            "expenses": "$" + entry_expenses
        }
        entries.append(new_entry)
        print("------------------")
        print("Congrats! You just recoreded a new entry! Keep it up!")
        print(new_entry)


    elif operation == "Show":
        print("------------------")
        print("Showing your entries:")
        print("------------------")
        for entry in entries:
            print(">>>" + entry["category"] + ": " + entry["expenses"])





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
