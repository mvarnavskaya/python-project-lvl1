#!/usr/bin/env python
from random import randint


WELCOME = 'What number is missing in the progression?'
LEN_PROGRESS_MAX = 10

def gsd(a, b):
    if b == 0:
        return a
    return gsd(b, a % b)


def generation():
    start_progress = randint(0, 10)
    len_progress = randint(5, LEN_PROGRESS_MAX - 1)
    step_progress = randint(0, 10)
    progression = [start_progress + i * step_progress
                   for i in range(0, len_progress - 1)]
    secret_key = randint(0, len_progress - 1)
    correct_answer = progression[secret_key]
    progression[secret_key] = '..'
    for i, _ in enumerate(progression):
        if i < len_progress - 1:
            progression[i] = str(progression[i]) + ' '
        progression[i] = str(progression[i])
    question = ''.join(progression)
    return question, str(correct_answer)
