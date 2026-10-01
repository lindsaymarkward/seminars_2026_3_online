"""Docstring"""

age = int(input("Age: "))
if age >= 65:
    is_qualified = True
else:
    is_qualified = False
print("...")
if is_qualified:
    print("You get a discount!")
