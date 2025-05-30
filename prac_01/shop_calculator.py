DISCOUNT = 0.9
number_of_item = int(input("Number of items: "))
while number_of_item < 0:
    print("Invalid number of items!")
    number_of_item = int(input("Number of items: "))
total = 0
for i in range(number_of_item):
    price_of_item = float(input("Price of item: "))
    total += price_of_item
if total >= 100:
    total *= DISCOUNT
print(f"Total price for {number_of_item} items is ${total:.2f}")
