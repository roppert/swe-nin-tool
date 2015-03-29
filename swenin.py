#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Creates a valid national identification number for
Sweden (personal identity number, called personnummer in swedish)

http://sv.wikipedia.org/wiki/Personnummer_i_Sverige
http://en.wikipedia.org/wiki/Personal_identity_number_%28Sweden%29
"""
from random import randint
from datetime import datetime, timedelta


def get_random_date_of_birth():
    age = (randint(18, 65) * 365) + randint(-182, 182)
    date = datetime.now() - timedelta(days=age)
    y = date.year
    m = date.month
    d = date.day
    return "".join(["{0:{fill}{width}}".format(x, fill=0, width=2) for x in [y, m, d]])


def get_random_number_of_birth():
    n = randint(1, 999)
    n = "{0:{fill}{width}}".format(n, fill=0, width=3)
    return n


def get_control_digit(date_of_birth, number_of_birth):
    factor = 2
    digits = ""
    for n in date_of_birth + number_of_birth:
        digits += str(int(n) * factor)
        factor = 1 if factor == 2 else 2

    sum = 0
    for n in digits:
        sum += int(n)

    control_digit = 10 - (sum % 10)
    control_digit = control_digit if control_digit < 10 else 0

    return str(control_digit)


def get_punctuation_for_date(date):
    year = int(date[:4])
    age = datetime.now().year - year
    return "-" if age < 100 else "+"


if __name__ == '__main__':
    import sys

    if len(sys.argv) == 2:
        date_of_birth = sys.argv[1]
    else:
        date_of_birth = get_random_date_of_birth()

    number_of_birth = get_random_number_of_birth()
    control_digit = get_control_digit(date_of_birth[2:],
                                      number_of_birth)
    punctuation = get_punctuation_for_date(date_of_birth)

    print("".join([date_of_birth, punctuation, number_of_birth, control_digit]))

# vi: set fileencoding=utf-8 :
