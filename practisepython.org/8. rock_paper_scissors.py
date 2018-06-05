import sys
import random
manual = "First type 2 for game start,\n then Type 1 for rock\n Type 2 for paper\n Type 3 for scissors\n type Q for quit"

while True:
    usr_command = input("Type:\n 1 - for manual\n 2 - for game start\n")
    if usr_command == "q":
        break
    elif usr_command == 2:
        p1 = input("Player 1 choose(1 - rock; 2 - paper; 3 - scissors)")
        p2 = input("Player 2 choose(1 - rock; 2 - paper; 3 - scissors)")
    elif usr_command == 1:
        print(manual)
    else:
        print("provided wrong command")
        break

print("Won: ")