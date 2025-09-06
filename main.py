import random
playing = True
number=str(random.randint(10,20))
print("i will generate an number from 10, 20 which you will try to guess")
print("the game ends when you get 1 hero")
while playing:
    guess=int(input("please enter your best guess"))
    if number==guess:
        print("you have guessed it right")
        print("the number was", number)
        break
    else:
        print("the number which you guessed was not right")