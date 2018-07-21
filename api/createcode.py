# -*- coding: utf-8 -*-

from random import randint

def create_one():
    i = randint(0, 9)
    i = str(i)
    return i


def create_code():
    code = ''
    for i in range(0, 6):
        code += create_one()
    return code

if __name__ == "__main__":
    create_code()