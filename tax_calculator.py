def calculate_income_tax(income):
    if income <= 10000:
        tax = 0
    elif income <= 20000:
        tax = 0.1 * (income - 10000)
    else:
        tax = 0.1 * 10000 + 0.2 * (income - 20000)
    return tax
