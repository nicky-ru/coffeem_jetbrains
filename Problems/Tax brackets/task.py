income = int(input())
percent = 0
if income >= 132407:
    percent = 28
elif income >= 42708:
    percent = 25
elif income >= 15528:
    percent = 15
calculated_tax = income * percent / 100

print("The tax for {} is {}%. That is {:.0f} dollars!".format(income, percent, calculated_tax))
