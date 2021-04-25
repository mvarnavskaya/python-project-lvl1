#!/usr/bin/env python
import random
import prompt


def welcome():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def is_even(number):
    return number % 2 == 0


def is_parity():
    name = welcome()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
        question = random.randint(0, 100000)
        print(f'Question: {question}')
        answer = prompt.string('Your answer:')

        if (is_even(question) and answer == 'yes')\
                or (not is_even(question) and answer == 'no'):
            print('Correct!')
            count += 1
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
