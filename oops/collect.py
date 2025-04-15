from collections import Counter

inventory = Counter(apple=50, mango=100, bananna=120, orange=70)

def update_inventory(order):
     inventory.subtract(order)

order = Counter(apple=10, bananna=12, orange=5)

update_inventory(order)

print(inventory)

