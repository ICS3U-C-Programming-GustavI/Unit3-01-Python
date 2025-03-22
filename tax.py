#!/usr/bin/env python3
# Created by: Gustav I
# Created on: March 20, 2025
# This program calculates the tax price and total for Newfoundland and Labrador.

# Fixed tax rate for Newfoundland and Labrador
TAX_RATE = 15

# Get user input
subtotal = float(input("Enter the subtotal: "))

# Calculations for tax amount and the total cost
tax_amount = (subtotal * TAX_RATE) / 100
total = subtotal + tax_amount

# Output messages highlighting tax and total cost
print(f"Tax: ${tax_amount:.2f}")
print(f"Total including tax: ${total:.2f}")
