#!/usr/bin/env python
from random import randint


WELCOME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num < 2:
        return 'yes'
    i = 2
    while i <= num / 2:
        if num % i == 0:
            return 'no'
        i += 1
    return 'yes'


def generation():
    question = randint(0, 100000)
    correct_answer = is_prime(question)
    return question, correct_answer
