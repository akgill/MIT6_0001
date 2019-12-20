#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 21:46:10 2019

@author: akgill
"""

PORTION_DOWN_PAYMENT = 0.25
TOTAL_COST = 1000000.0
MONTHS=36
R=0.04
SEMI_ANNUAL_RAISE=0.07


def how_much_to_save_monthly():
    starting_salary = float(input("Enter your starting salary: "))
    savings_needed = TOTAL_COST * PORTION_DOWN_PAYMENT
    
    # guesses in units of ten thousandths
    low_guess = 0  # 0.00% monthly savings rate
    high_guess = 10000  # 100.00% monthly savings rate
    
    # Before bisection search, check that it is possible to save enough at 100%
    # savings rate. If not, quit early.
    if (savings(starting_salary, high_guess/10000) < savings_needed):
        print("It is not possible to pay the down payment in three years.")
        return
    
    mid_savings = 0
    steps = 0
    while (abs(mid_savings - savings_needed) > 100):
        steps += 1
        mid_guess = ((high_guess - low_guess) // 2) + low_guess
        mid_savings = savings(starting_salary, mid_guess/10000)
        
        if (mid_savings < savings_needed):
            low_guess = mid_guess
            
        if (mid_savings > savings_needed):
            high_guess = mid_guess    
    
    print("Best savings rate: ", mid_guess/10000)
    print("Steps in bisection search: ", steps)

    
def savings(annual_salary=0, portion_saved=0):
    current_savings = 0
    for month in range(0, MONTHS):
        current_savings += (annual_salary / 12.0) * portion_saved
        current_savings += current_savings * R / 12.0
        if (month % 6 == 0):
            annual_salary += annual_salary * SEMI_ANNUAL_RAISE
    
    return current_savings