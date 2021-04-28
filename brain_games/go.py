#!/usr/bin/env python
from brain_games.cli import welcome_user
import prompt


COUNT = 3


def engine(module):
    name = welcome_user()
    print(module.WELCOME)
    i = 1
    while i <= COUNT:
        question, correct_answer = module.generation()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f" Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        i += 1
    print(f'Congratulations, {name}!')
