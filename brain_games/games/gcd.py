#!/usr/bin/env python
from random import randint


WELCOME = 'Find the greatest common divisor of given numbers.'


def gsd(a, b):
    if b == 0:
        return a
    return gsd(b, a % b)


def generation():
    question1 = randint(0, 100000)
    question2 = randint(0, 100000)
    correct_answer = gsd(question1, question2)
    return f'{question1} {question2}', correct_answer
