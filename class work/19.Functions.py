data={'current balance': 5000, 'history': []}
def menu():
    print('\n[C]heck Balance')
    print('[D]eposit')
    print('[W]ithdraw')
    print('[V]iew Transaction History')
    print('[E]xit\n')
def Welcome():
    print('Welcome to ATM'.center(40,'*'))

def Check_Balance():
    print (f'Current Balance: ${data["current_balance"]}')


def  Withdraw():
    amount=int(input("Enter the amount to withdraw: "))
    if amount<=data['current_balance']:
       data['current_balance']-=amount
       data['history'].append(f'Withdraw: ${amount}')
       print(f'${amount} is successfully Withdraw!!!!')
    else:
        print('Insufficient Balance')

def Deposit():
    amount=int(input("Enter the amount to deposit: "))
    data['current_balance']+=amount
    data['history'].append(f'Deposited: ${amount}')
    print (f'${amount} is successfully deposited!!!')

def View_History():
    if data['history']:
       print('Transaction History'.center (40,'-'))
       for i in data['history']:
             print(i)
       else:
           print("No Transactions")

def Flow_Check (ch):
    if ch=='C':
        Check_Balance ()
    elif ch=='D':
        Deposit ()
    elif ch=='W':
        Withdraw()
    elif ch=='V':
        View_History()


Welcome()
while True:
    menu ()
    ch=input ("Enter the char[CDWVE]: ").upper()
    Flow_Check(ch)
    elif ch == 'E':
        print("Thankyou " center(40,'.'))
        break
    else:
    print("Invalid choice")