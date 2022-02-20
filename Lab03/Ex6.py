prov_id = input("Please enter your province's two-letter abbreviation (e.g., AB for Alberta): ")
gross_income = float(input("Please enter your taxable income: "))

if prov_id.lower() == "ab":
    if gross_income < 40000.01:
        tax_rate = 0.25
    elif gross_income < 80000.01:
        tax_rate = 0.32
    elif gross_income < 120000.01:
        tax_rate = 0.36
    else:
        tax_rate = 0.39

elif prov_id.lower() == "bc":
    if gross_income < 20000.01:
        tax_rate = 0.2
    elif gross_income < 35000.01:
        tax_rate = 0.225
    elif gross_income < 50000.01:
        tax_rate = 0.30
    elif gross_income < 65000.01:
        tax_rate = 0.325
    elif gross_income < 80000.01:
        tax_rate = 0.365
    elif gross_income < 100000.01:
        tax_rate = 0.393
    elif gross_income < 120000.01:
        tax_rate = 0.41
    else:
        tax_rate = 0.44

elif prov_id.lower() == "on" or "sk":
    if gross_income < 40000.01:
        tax_rate = 0.25
    elif gross_income < 60000.01:
        tax_rate = 0.30
    elif gross_income < 80000.01:
        tax_rate = 0.35
    elif gross_income < 100000.01:
        tax_rate = 0.40
    elif gross_income < 120000.01:
        tax_rate = 0.45
    else:
        tax_rate = 0.50

print("Province: " + prov_id.lower())
print("Gross Income: " + str(gross_income))
print("Tax Rate: " + str(tax_rate))
print("Tax Amount: " + str(gross_income * tax_rate))
print("Net Income: " + str(gross_income * (1 - tax_rate)))
