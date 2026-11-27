name = input("Customer name: ") 
balance = float(input("Initial account balance: Rs. "))

if balance < 0: print("Balance cannot be negative")
raise SystemExit 
choice = input("Enter D for deposit or W for withdrawal: ").strip().upper() 
amount = float(input("Enter amount: Rs. ")) 
if amount <= 0:   
   print("Amount must be positive")
elif choice == "D": 
      balance += amount   
      print("Deposit successful")
elif choice == "W":   
    if balance - amount < 2000:     
        print("Withdrawal denied: minimum balance of Rs. 2000 must remain")   
    else:balance -= amount     
print("Withdrawal successful") 
print("Invalid operation")   
print("Customer:", name) 
print("Updated balance: Rs.", balance) 