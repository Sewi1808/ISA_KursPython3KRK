

def search_in_data():
    import sys
    import json
    data = json.load(open("data.json"))
    user_entry = input('Provide data to find: \n').lower()
    while True:
        if user_entry == 'q':
            print("Program Exit")
            sys.exit()
        elif user_entry not in data:
            print("You provide wrong data, try again")
            search_in_data()
        else:
            print(data[user_entry])
            search_in_data()


search_in_data()
# print(data['rain'])
