#!/usr/bin/env python

# name    :  cash_flow.py
# version :  0.0.1
# date    :  20240318
# author  :  Leam Hall
# desc    :  Trying to figure out how long we can last without a job.


""" Given integers for monthly expenses and income, along with current
    savings and annual expenses, show how many months of bills can be paid.
"""

from argparse import ArgumentParser


def per_month(out, income, savings, annual):
    """Returns an int of how much is left in monthly savings."""
    return int(savings + income - out - (annual / 12))


parser = ArgumentParser()
parser.add_argument("-o", "--out", help="Money going out", default=1, type=int)
parser.add_argument("-s", "--savings", help="Savings", default=0, type=int)
parser.add_argument(
    "-i", "--income", help="Money coming in", default=0, type=int
)
parser.add_argument(
    "-a", "--annual", help="Annual expenses", default=0, type=int
)
args = parser.parse_args()

MAX_TEST = 24
months = 0
have_enough = True
savings = args.savings

while have_enough:
    if months > MAX_TEST:
        break
    savings = per_month(args.out, args.income, savings, args.annual)
    if savings < args.out:
        have_enough = False
    else:
        months += 1

month_word = "months"
if months == 1:
    month_word = "month"
elif months >= MAX_TEST:
    months = "more than {}".format(MAX_TEST)

print("You have enough for {} {}.".format(months, month_word))
