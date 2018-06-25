import csv
import json
import os
import pdb

from app import write_entries_to_file

entry = [
    {'year': '2018', 'month': '06', 'day': '25', 'category': 'snacks', 'expense': '12'},
    {'year': '2018', 'month': '06', 'day': '24', 'category': 'meals', 'expense': '25'},
    {'year': '2018', 'month': '06', 'day': '23', 'category': 'stationary', 'expense': '16'},
]

def test_write_entries_to_file():
    #setup:
    write_entries_to_file(entries=entry, filname="tests\example_data.csv")
    #test:
    csv_filepath = os.path.join(os.path.dirname(__file__), "example_data.csv")
    rows_written = []
    with open(csv_filepath, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            rows_written.append(dict(row))
    assert len(rows_written) == 3
    assert rows_written[0]["year"] == "2018"
    assert rows_written[0]["month"] == "06"
    assert rows_written[0]["day"] == "25"
    assert rows_written[0]["category"] == "snacks"
    assert rows_written[0]["expense"] == "12"
