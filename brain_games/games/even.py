#!/usr/bin/env python
from random import randint


WELCOME = 'Answer "yes" if number even otherwise answer "no".'


def is_even(number):
    return 'yes' if number % 2 == 0 else 'no'


def generation():
    question = randint(0, 100000)
    correct_answer = is_even(question)
    return question, correct_answer
