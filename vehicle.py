vehicle_type = input("Vehicle type (two-wheeler/four-wheeler/heavy vehicle): ").strip().lower()
vehicle_number = input("Vehicle number: ").strip()
hours = float(input("Parking duration in hours: "))
rates = { "two-wheeler": 20, "four-wheeler": 50, "heavy vehicle": 100 }
if vehicle_type not in rates:
    print("Invalid vehicle type")
elif hours < 0:
    print("Hours cannot be negative")
else:
    fee = rates[vehicle_type] * hours
    print("Vehicle type:", vehicle_type)
    print("Vehicle number:", vehicle_number)
    print("Parking duration:", hours, "hours")
    print("Total parking fee: Rs.", fee)
    print("Thank you for using our parking service!")