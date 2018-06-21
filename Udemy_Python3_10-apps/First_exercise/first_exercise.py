import json
import sys
import difflib


def search_in_data():
    data = json.load(open("data.json"))
    user_entry = input('Provide data to find(for quit type "Q": \n').lower()
    if user_entry == 'q':
        print("Program Exit")
        sys.exit()
    elif user_entry not in data:
        print("You provide wrong data")
        print("maybe you meant: \n", difflib.get_close_matches(user_entry, data.keys(), n=1))
        search_in_data()
    else:
        return data[user_entry]


print(search_in_data())
