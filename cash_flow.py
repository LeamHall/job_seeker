#!/usr/bin/env python

# name    :  cash_flow.py
# version :  0.0.1
# date    :  20240318
# author  :  Leam Hall
# desc    :  Trying to figure out how long we can last without a job.

# TODO:
#   Add an "annual expenses" argument, and pay 1/12 per month.
#   pytest
#   mypy
#   flake8 and black


from argparse import ArgumentParser


def per_month(out, income, savings):
    return savings + income - out


parser = ArgumentParser()
parser.add_argument("-o", "--out", help="Money going out", default=1, type=int)
parser.add_argument("-s", "--savings", help="Savings", default=0, type=int)
parser.add_argument(
    "-i", "--income", help="Money coming in", default=0, type=int
)
args = parser.parse_args()

months = 0
have_enough = True
savings = args.savings

while have_enough:
    savings = per_month(args.out, args.income, savings)
    if savings < args.out:
        have_enough = False
    months += 1

print("You have enough for {} months.".format(months))
