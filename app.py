import csv
import os
import json
from dotenv import load_dotenv
import requests


def menu(username="iriskhu"):
    ## this is a multi-line string, also using preceding `f` for string interpolation---Prof.'s notes
    menu = f"""
    ------------------------------------
            SaveMore Bookkeeping
    ------------------------------------
    Hi {username}, welcome to SaveMore!
    Here you can record your expenses, calculate the total, and convert it to another currency. Let's get start it!
        operation  | description
        ---------  | ------------------
        'Record'   | Record each one of your expenses
        'Show'     | Show all the recorded entries
        'Update'   | Edit an existing entry.
        'Calculate'| Calculate the total of your entries
        'Convert'  | Convert an amount to another currency
        'Clear'    | Clear all your records.

    Please select an operation: """ ## end of multi- line string. also using string interpolation---Prof.'s notes
    return menu

#http://www.apilayer.net/api/live?access_key=5cbfe5f30bd5dd43f988b7941ddb967c&format=1

def parse_response(response_text):

    if isinstance(response_text, str): ## checking to see if the datatype of "response_text" is string---if not, then:
        response_text = json.loads(response_text) ## converting the string to a dictionary.

    results = []
    exchange_rate = response_text["quotes"] ## which is a nested dictionary
    for rates in exchange_rate: ## using for loop to loop through the dictionary's top-level keys/attributes
        print(rates)

#        prices = time_series_daily[trading_date] #> {'1. open': '101.0924', '2. high': '101.9500', '3. low': '100.5400', '4. close': '101.6300', '5. volume': '22165128'}
#        result = {
#            "date": trading_date,
#            "open": prices["1. open"],
#            "high": prices["2. high"],
#            "low": prices["3. low"],
##            "volume": prices["5. volume"]
#        } ## creating a new dictionary to store initial prices
#        results.append(result)
    return results




def read_entries_from_file(filename = "entries.csv"):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    print(f"READING PRODUCTS FROM FILE: '{filepath}'")
    entries = [] ## the next commands are to open the file and populate the products list with product dictionaries)
    with open(filepath, "r") as csv_file: ## to open file "filepath"
        reader = csv.DictReader(csv_file) ## to assume your CSV has headers
        for ordered_dict in reader:
            entries.append(dict(ordered_dict)) ## append.() function: adding stuff to the row
    return entries

def write_entries_to_file(filename="entries.csv", entries=[]):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    #print(f"OVERWRITING CONTENTS OF FILE: '{filepath}' \n ... WITH {len(products)} PRODUCTS")
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


def run():
## the run function here is to specify which function is going wrong

    #...to read products from file...
    entries = read_entries_from_file()

    #...to prompt the user to select an operation...
    #number_of_products = len(products) ## reference: in-class workshop
    my_menu = menu(username="iriskhu")
    operation = input(my_menu)
    print("YOU CHOSE: " + operation)


    operation = operation.title()

    if operation == "Record":
        print("------------------")
        entry_year = input ("What yaer? " )
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

    elif operation == "Clear":
        print("------------------------")
        clear_entries_file()


    elif operation == "Convert":
        load_dotenv()

        api_key = os.environ.get("currencylayer_api_key") or "OOPS. Please set an environment variable named 'currencylayer_api_key'."
        print(api_key)

        abbreviation


    else:
        print("------------------")
        print("Oops, unrecognized operation, please try again.")
        print("----------------------")
        write_entries_to_file(entries=entries)


if __name__ == "__main__":
    run()