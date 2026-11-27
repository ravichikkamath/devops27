RATE = 98 
def inr_to_usd(inr):  
       return inr / RATE   
def usd_to_inr(usd):  
       return usd * RATE  
       if __name__ == "__main__":   
          choice = input("1. INR to USD  2. USD to INR: ")   
          amount = float(input("Enter amount: "))   
          if amount < 0:      
               print("Amount cannot be negative")    
          elif choice == "1":     
               print("USD:", round(inr_to_usd(amount), 2))   
          elif choice == "2":   
               print("INR: Rs.", round(usd_to_inr(amount), 2))  
          else:       
               print("Invalid choice") 