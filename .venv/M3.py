# Calculates federal income and FICA (social security and Medicare) from various tax brackets based on filing statuses
def us_tax_amount(gross_income, filing_status):
    if filing_status == "single":
        taxable_income = max(0, gross_income - 15750)

        if taxable_income <= 11925:
            tax = 0.1 * taxable_income
        elif taxable_income <= 48475:
            tax = 0.1 * 11925 + 0.12 * (taxable_income - 11925)
        elif taxable_income <= 103350:
            tax = 0.1 * 11925 + 0.12 * 36550 + 0.22 * (taxable_income - 48475)
        elif taxable_income <= 197300:
            tax = 0.1 * 11925 + 0.12 * 36550 + 0.22 * 54875 + 0.24 * (taxable_income - 103350)
        elif taxable_income <= 250525:
            tax = 0.1 * 11925 + 0.12 * 36550 + 0.22 * 54875 + 0.24 * 93950 + 0.32 * (taxable_income - 197300)
        elif taxable_income <= 626350:
            tax = 0.1 * 11925 + 0.12 * 36550 + 0.22 * 54875 + 0.24 * 93950 + 0.32 * 53225 + 0.35 * (
                        taxable_income - 250525)
        else:
            tax = 0.1 * 11925 + 0.12 * 36550 + 0.22 * 54875 + 0.24 * 93950 + 0.32 * 53225 + 0.35 * 375825 + 0.37 * (
                        taxable_income - 626350)

        if gross_income <= 200000:
            fica = 0.062 * min(gross_income, 184500) + 0.0145 * gross_income
        else:
            fica = 0.062 * min(gross_income, 184500) + 0.0145 * 200000 + 0.0235 * (gross_income - 200000)

        return round(tax + fica)

    elif filing_status == "jointly":
        taxable_income = max(0, gross_income - 31500)

        if taxable_income <= 23850:
            tax = 0.1 * taxable_income
        elif taxable_income <= 96950:
            tax = 0.1 * 23850 + 0.12 * (taxable_income - 23850)
        elif taxable_income <= 206700:
            tax = 0.1 * 23850 + 0.12 * 73100 + 0.22 * (taxable_income - 96950)
        elif taxable_income <= 394600:
            tax = 0.1 * 23850 + 0.12 * 73100 + 0.22 * 109750 + 0.24 * (taxable_income - 206700)
        elif taxable_income <= 501050:
            tax = 0.1 * 23850 + 0.12 * 73100 + 0.22 * 109750 + 0.24 * 187900 + 0.32 * (taxable_income - 394600)
        elif taxable_income <= 751600:
            tax = 0.1 * 23850 + 0.12 * 73100 + 0.22 * 109750 + 0.24 * 187900 + 0.32 * 106450 + 0.35 * (
                        taxable_income - 501050)
        else:
            tax = 0.1 * 23850 + 0.12 * 73100 + 0.22 * 109750 + 0.24 * 187900 + 0.32 * 106450 + 0.35 * 250550 + 0.37 * (
                        taxable_income - 751600)

        if gross_income <= 250000:
            fica = 0.062 * min(gross_income, 184500) + 0.0145 * gross_income
        else:
            fica = 0.062 * min(gross_income, 184500) + 0.0145 * 250000 + 0.0235 * (gross_income - 250000)

        return round(tax + fica)

    elif filing_status == "head":
        taxable_income = max(0, gross_income - 23625)

        if taxable_income <= 17000:
            tax = 0.1 * taxable_income
        elif taxable_income <= 64850:
            tax = 0.1 * 17000 + 0.12 * (taxable_income - 17000)
        elif taxable_income <= 103350:
            tax = 0.1 * 17000 + 0.12 * 47850 + 0.22 * (taxable_income - 64850)
        elif taxable_income <= 197300:
            tax = 0.1 * 17000 + 0.12 * 47850 + 0.22 * 38500 + 0.24 * (taxable_income - 103350)
        elif taxable_income <= 250500:
            tax = 0.1 * 17000 + 0.12 * 47850 + 0.22 * 38500 + 0.24 * 93950 + 0.32 * (taxable_income - 197300)
        elif taxable_income <= 626350:
            tax = 0.1 * 17000 + 0.12 * 47850 + 0.22 * 38500 + 0.24 * 93950 + 0.32 * 53200 + 0.35 * (
                        taxable_income - 250500)
        else:
            tax = 0.1 * 17000 + 0.12 * 47850 + 0.22 * 38500 + 0.24 * 93950 + 0.32 * 53200 + 0.35 * 375850 + 0.37 * (
                        taxable_income - 626350)

        if gross_income <= 200000:
            fica = 0.062 * min(gross_income, 184500) + 0.0145 * gross_income
        else:
            fica = 0.062 * min(gross_income, 184500) + 0.0145 * 200000 + 0.0235 * (gross_income - 200000)

        return round(tax + fica)

    else:
        raise ValueError("filing_status should be 'single' or 'jointly' or 'head'")


# Calculates tax-free Personal Allowance and National Income Contributions from various tax brackets
def uk_tax_amount(gross_income):
    personal_allowance = 12570
    if gross_income > 100000:
        reduction = (gross_income - 100000) / 2
        personal_allowance = max(0, personal_allowance - reduction)
    taxable_income = max(0, gross_income - personal_allowance)

    if taxable_income <= 37700:
        tax = 0.2 * taxable_income
    elif taxable_income <= 125140:
        tax = 0.2 * 37700 + 0.4 * (taxable_income - 37700)
    else:
        tax = 0.2 * 37700 + 0.4 * 87440 + 0.45 * (taxable_income - 125140)

    if gross_income <= 12570:
        nic = 0
    elif gross_income <= 50270:
        nic = 0.08 * (gross_income - 12570)
    else:
        nic = 0.08 * 37700 + 0.02 * (gross_income - 50270)

    return round(tax + nic)


# Determines percentage of post-tax income spent on essential expenditures by age group in the U.S., and multiplies that value by total post-tax income
def us_disposable_income(gross_income, filing_status, age):
    if age < 25:
        scalar = 43417 / (48514 - us_tax_amount(48514, filing_status))
        disposable_income = (1 - scalar) * (gross_income - us_tax_amount(gross_income, filing_status))
    elif age < 35:
        scalar = 66976 / (102494 - us_tax_amount(102494, filing_status))
        disposable_income = (1 - scalar) * (gross_income - us_tax_amount(gross_income, filing_status))
    elif age < 45:
        scalar = 81918 / (128285 - us_tax_amount(128285, filing_status))
        disposable_income = (1 - scalar) * (gross_income - us_tax_amount(gross_income, filing_status))
    elif age < 55:
        scalar = 88127 / (141121 - us_tax_amount(141121, filing_status))
        disposable_income = (1 - scalar) * (gross_income - us_tax_amount(gross_income, filing_status))
    elif age < 65:
        scalar = 75089 / (121571 - us_tax_amount(121571, filing_status))
        disposable_income = (1 - scalar) * (gross_income - us_tax_amount(gross_income, filing_status))
    elif age < 75:
        scalar = 56379 / (75460 - us_tax_amount(75460, filing_status))
        disposable_income = (1 - scalar) * (gross_income - us_tax_amount(gross_income, filing_status))
    else:
        scalar = 47144 / (56028 - us_tax_amount(56028, filing_status))
        disposable_income = (1 - scalar) * (gross_income - us_tax_amount(gross_income, filing_status))

    return round(disposable_income)


# Determines percentage of post-tax income spent on essential expenditures by age group in the UK, and multiplies that value by total post-tax income
def uk_disposable_income(gross_income, age):
    if age < 30:
        scalar = 16452.8 / (28515 - uk_tax_amount(28515))
        disposable_income = (1 - scalar) * (gross_income - uk_tax_amount(gross_income))
    elif age < 50:
        scalar = 16463.2 / (48016 - uk_tax_amount(48016))
        disposable_income = (1 - scalar) * (gross_income - uk_tax_amount(gross_income))
    elif age < 65:
        scalar = 15574 / (41866 - uk_tax_amount(41866))
        disposable_income = (1 - scalar) * (gross_income - uk_tax_amount(gross_income))
    elif age < 75:
        scalar = 11944.4 / (36036 - uk_tax_amount(36036))
        disposable_income = (1 - scalar) * (gross_income - uk_tax_amount(gross_income))
    else:
        scalar = 9474.4 / (18600 - uk_tax_amount(18600))
        disposable_income = (1 - scalar) * (gross_income - uk_tax_amount(gross_income))

    return round(disposable_income)


# Sample scenarios for the U.S.
print(us_disposable_income(45300, "single", 24))
print(us_disposable_income(94000, "jointly", 30))
print(us_disposable_income(65800, "head", 40))
print(us_disposable_income(90100, "single", 50))
print(us_disposable_income(310500, "jointly", 60))
print(us_disposable_income(120000, "jointly", 70))
print(us_disposable_income(35700, "single", 80))

print("") # Skip Line

# Sample scenarios for the UK
print(uk_disposable_income(40400, 25))
print(uk_disposable_income(170500, 45))
print(uk_disposable_income(110200, 55))
print(uk_disposable_income(480600, 70))
print(uk_disposable_income(29900, 80))