#!/usr/bin/env python
from random import randint


WELCOME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num < 2:
        return 'no'
    i = 2
    while i <= num / 2:
        if num % i == 0:
            return 'yes'
        i += 1
    return 'no'


def generation():
    question = randint(0, 100000)
    correct_answer = is_prime(question)
    return question, correct_answer
