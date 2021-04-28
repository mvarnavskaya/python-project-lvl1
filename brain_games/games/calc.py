#!/usr/bin/env python
from random import randint, choice
from operator import add, sub, mul


WELCOME = 'What is the result of the expression?'


OPERATIONS = (('+', add), ('-', sub), ('*', mul))


def generation():
    number1 = randint(1, 10)
    number2 = randint(1, 10)
    symbol, operation = choice(OPERATIONS)
    question = '{} {} {}'.format(number1, symbol, number2)
    answer = operation(number1, number2)
    return question, str(answer)
