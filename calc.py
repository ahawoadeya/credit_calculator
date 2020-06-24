
import argparse
import sys
from math import ceil, log


def diff_payment(principal, periods, interest):
    nominal_rate = interest / (12 * 100)
    overpayment = 0
    for payment_months in range(1, periods + 1):
        payment = ceil(
            (principal / periods) + nominal_rate * (principal - (principal * (payment_months - 1)) / periods))
        overpayment += payment
        print(f'Month {payment_months}: paid out {payment}')
    return f'Overpayment = {ceil(overpayment - principal)}'


def count_of_months(principal, monthly, interest):
    nominal_rate = interest / (12 * 100)
    period_count = ceil(log(monthly / (monthly - nominal_rate * principal), 1 + nominal_rate))
    if period_count < 12:
        print(f'You need {period_count} months to repay this credit!')
        return f'Overpayment = {ceil((monthly * period_count) - principal)}'
    elif period_count % 12 == 0:
        print(f'You need {period_count // 12} years to repay this credit!')
        return f'Overpayment = {ceil((monthly * period_count) - principal)}'
    else:
        print(f'You need {period_count // 12} years and {period_count % 12} months to repay this credit!')
        return f'Overpayment = {ceil((monthly * period_count) - principal)}'


def annuity_payment(principal, periods, interest):
    nominal_rate = interest / (12 * 100)
    payment = ceil(
        principal * (nominal_rate * pow((1 + nominal_rate), periods)) / (pow((1 + nominal_rate), periods) - 1))
    print(f'Your annuity payment = {payment}!')
    return f'Overpayment = {ceil((payment * periods) - principal)}'
