import json
import sys
import difflib

data = json.load(open("data.json"))


def print_output():
    for item in output:
        print(item)


def search_in_data(inp):
    if inp == 'q':
        print("Program Exit")
        sys.exit()
    elif inp in data:
        return data[inp]
    elif len(difflib.get_close_matches(inp, data.keys())) > 0:
        y_n = input("Did you mean \n %s \n do you want to use it (y/n): \n" %
                    difflib.get_close_matches(user_entry, data.keys())[0]).lower()
        if y_n == 'y':
            return data[difflib.get_close_matches(inp, data.keys())[0]]
        elif y_n == 'n':
            return "The word doesn't exist. (n)"

        else:
            return "command not recognized"
    else:
        return "The word doesn't exist (2)"


user_entry = input('Provide data to find(for quit type "Q": \n').lower()

output = search_in_data(user_entry)

print_output()
