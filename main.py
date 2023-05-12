import random as r
print("welcome to the guessing game!")
first=int(input("enter the first number of the range: "))
last=int(input("enter the last number of the range: "))
x = r.randint(first, last)
while True:
    guess=int(input("guess a number between 1 and 100: "))
    while True:
        if guess==x:
            print("right guess, would you like to play another game? y/n: ")
            break
        elif guess!=x:
            print("wrong guess, try again")
            guess=int(input("guess a number between 1 and 100: "))
    answer = input()
    if answer == "n":
        print("thank you for playing our game!")
        break
    elif answer == "y":
        x = r.randint(first, last)
        continue
    break