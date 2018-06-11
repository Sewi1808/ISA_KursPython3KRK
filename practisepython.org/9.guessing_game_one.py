import random

#Guessing game

#get random num
r_num = random.randint(1,9)
# 0 value guess
guess = 0
# 0 value count
count = 0

while guess != r_num and guess != "exit":
    guess = input("Guess number in range of 1 to 9: \n")

    if guess == "exit":
        break

    guess = int(guess)
    count +=1

    if guess < r_num:
        print("your guess was to low! \n :(")
    elif guess > r_num:
        print("Guess to high! \n:<")
    else:
        print("You lucky bustard!")
        print(f"you won with only {count} tries!")