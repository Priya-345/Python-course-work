data = {
    'current_balance':5000,
    'history':[]
}

def Menu():
    print("1.[c]current balance")
    print("2.[d]deposit")
    print("3.[w]withdraw")
    print("4.[v]view Transaction History")
    print("[E]Exit")
    
def Welcome():
    print(" Welcome to ATM ".center(40,'*'))  
    
    
def Check_Balance():
    print(f'Current balance ${data["current_balance"]}') 
def Deposit():
    amount = int(input("Enter amount to deposit : "))
    data['current_balance']+= amount
    data['history'].append(f'Deposited: ${amount}')
    print(f'${amount} is sucsessfully Deposited!!!')
def Withdraw():
    amount = int(input("Enter the amount to withdraw:"))
    if amount<=data['current_balance']:
        data['current_balance']-=amount
        data['history'].append(f'withdraw : ${amount}')
        print(f'${amount} is successfully deposited!!!')
def  View_History():
    if data['history']:
        print("Transaction History".center(40,'-'))
        for i in data['history']:
            print(i)
            print("End of History".center(40,'*'))
            
             
def Flow_check():
    if ch == 'C':
       Check_Balance()
    elif ch =='D':
        Deposit()
    elif ch == 'W':
        Withdraw()
    elif ch == 'V':
      View_History()
    
    

Welcome()
while True:
  Menu()   
  ch = input("Enter the char[CDWVE]: ").upper()
  if ch == 'C':
    Check_Balance()
  elif ch =='D':
      Deposit()
  elif ch == 'W':
      Withdraw()
  elif ch == 'V':
      View_History()
  elif ch == 'E':
      print("thankyou".center(40,'*'))
  else:
      print("Invalid choice")                
          
 