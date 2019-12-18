#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 20:45:24 2019

@author: akgill
"""

def months_required_a(portion_down_payment=0.25, current_savings=0, r=0.04):
    annual_salary = float(input("What is your annual salary?\n"))
    portion_saved = float(input("What fraction of your salary can you save each month? [0, 1]\n"))
    total_cost = float(input("What is the total cost of the house you'd like to buy?\n"))
    
    monthly_salary = annual_salary / 12.0
    monthly_savings = monthly_salary * portion_saved
    total_needed = total_cost * portion_down_payment
    
    months = 0
    current_savings = 0
    while (current_savings < total_needed):
        months += 1
        current_savings += monthly_savings
        current_savings += current_savings * r / 12
    
    print("Number of months ", months)