products = ["Shoes", "Clothes", "Smartphone", "Smart watch", "Bluetooth speaker"]
total = 0
for product in products:
    price = float(input(f"Enter price of {product}: Rs. "))
    if price < 0:
        print("Price cannot be negative")
        raise SystemExit
    total += price
print("Total purchase amount: Rs.", total) 