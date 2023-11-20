#!/usr/bin/env python3

def happy_new_year():
    counter = 10
    counter-= 1
    while (counter > 0):
       print("Happy New Year!")
    
    # code goes here!
happy_new_year()


def square_integers(int_list):
    squared_ints = [int_val ** 2 for int_val in int_list]
    return squared_ints

square_integers([1, 2, 3, 4, 5])

def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)


fizzbuzz()
