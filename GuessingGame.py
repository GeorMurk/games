#!/usr/bin/python

#!Guessing Game

secret_word = "lion"
guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False

while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter Secret Word: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("YOU LOOOOOOOOOOSSSSSEEEEE!!!!!!")
else:
    print("You Win!!!!")


#!Go ahead and test It Out!!!!
