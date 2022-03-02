#1) Storing a random number between 1-10 in a variable
import random
from re import A
from tkinter import E, FALSE
numb = random.randint(1,10)
user_name = input("what is your name? ")
user_guess = int(input(user_name + "! please, guess a number between 1 and 10: "))
if user_guess == numb:
    print("Bravo " + user_name + "! you guessed right" )
else:
    print("Wrong guess, try again")


#2) hear a joke with your favourite number
joke1 = str("What's a foot long and slippery? A slipper!")
joke2 = str("I invented a new word today: Plagiarism.")
joke3 = str("What did one traffic light say to the other? Stop looking at me, I'm changing!")
fav_numb = int(input("what is your favourite number?: "))
if fav_numb == 3:
    print(joke2)
elif fav_numb == 21:
    print(joke1)
elif fav_numb == 70:
    print(joke3)
elif fav_numb <= 1:
    print("invalid number")
elif fav_numb >= 100:
    print("invalid number")
else:
    print("Oops! not a lucky number, try again...")


#3) favourite meal
starter = input("what is your favourite starter?: ")
main_course = input("what is your favourite main course?: ")
dessert = input("what is your favourite desert?: ")
drink = input("what is your favourite drink?: ")
print("Your favourite meal is " + starter, main_course, dessert, "with a glass of " + drink) 


#4)Decline in value of a motorbike
j = 2000
while j > 1000:
    print("The value of motorbike is: ", j)
    j = j - j * 0.1
    print(j)


#5) Menu of choice of operator
add = str('a')
subtract = str('b')
divide = str('c')
multiply = str('d')
power_of = str('e')
first_numb = int(input("what is your first number?: "))
second_numb = int(input("what is your second number?: "))
operator = input("enter 'a' for add, 'b' for subtract, 'c' for divide, 'd' for multiply and 'e' for power of: ")
i = first_numb + second_numb
j = first_numb - second_numb
k = first_numb / second_numb
l = first_numb * second_numb
m = first_numb ** second_numb
if operator == add:
    print(i)
elif operator == subtract:
    print(j)
elif operator == divide:
    print(k)
elif operator == multiply:
    print(l)
elif operator == power_of:
    print(m)
else:
    print("Invalid operator command!")