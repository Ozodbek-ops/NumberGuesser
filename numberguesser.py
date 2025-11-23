import random

num = random.randint(1, 100)
guessed_num = 0
attempts = 0
while guessed_num != num:
    guessed_num = int(input("Guess the random number: "))
    attempts+=1
    if guessed_num>101 or guessed_num<1:
        print("Please, enter a number between 1 and 100")
    elif guessed_num == num:
        print(f"Congrats! Your guess was right. It took you {attempts} attempts!")
    elif guessed_num>num:
        print("Try lower!")
    elif guessed_num<num:
        print("Try higher!")
           
