import math

bill_generated = int(input("What is the total bill?\n£ "))

customers = int(input("How many people ate the food?\n"))

tip = math.ceil(bill_generated/customers)*1.12

print(f"Each person should pay £{tip}")
