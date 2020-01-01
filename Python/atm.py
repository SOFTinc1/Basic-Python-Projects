print('Welcome to UTILITY Bank')
print('insert your card')
restart = 'y'
balance = 300000
chance = 3
print('welcome Hussayn Abdulrahmon')
cus_pin = int(input('enter your pin '))
if cus_pin == (1234):
   while(cus_pin!=90000):
    print('welcome')
    #while restart not in('n','NO','no','N'):
    atm_menu = input('select option\n \n(a)Balance \n(b)Withdraw \n(c)Bills \n(d)Transfer\n')
    if (atm_menu.lower() == 'a'):
        print('your balance is', balance)
        restart = input('would you like to go back? ')
        if restart in('y','YES','yes','Y'):
            print('thank you')
        else:
            print('pls select a valid option')
    elif (atm_menu.lower() == 'b'):
        withdraw = input('select amount to withdraw\n \n(a)2000 \n(b)5000 \n(c)10000 \n(d)20000\t(e)other amount\t\n')
        if (withdraw.lower() == 'a'):
            print('pls take your cash')
            balance = balance - int(2000)
        elif(withdraw.lower() == 'b'):
            print('pls take your cash')
            balance = balance - int(5000)
        elif(withdraw.lower() == 'c'):
            print('pls take your cash')
            balance = balance - int(10000)
        elif(withdraw.lower() == 'd'):
            print('pls take your cash')
            balance = balance - int(20000)
        elif(withdraw.lower() == 'e'):
            ent_amount = int(input('enter amount: '))
            print('pls take your cash')
            balance = balance - ent_amount
        else:
            print('invalid selection')
        restart = input('would you like to go back? ')
        if restart in('y','YES','yes','Y'):
            print('thank you')
        else:
            print('pls select a valid option')
    elif (atm_menu.lower() == 'c'):
        bills = input('select option:\n \t(a)airtime\t(b)Electricity bill\t\n')
        if (bills.lower() == 'a'):
            amount = input('select amount:\n \t(a)100\t(b)200\t(c)500\t\n')
            if (amount.lower() == 'a'):
                number = int(input('enter your phone number: '))
                print('you have recharge',number,'with 100')
            elif (amount.lower() == 'b'):
                number = int(input('enter your phone number: '))
                print('you have recharge',number,'with 200')
            elif (amount.lower() == 'c'):
                number = int(input('enter your phone number: '))
                print('you have recharge',number,'with 500')
            else:
                print('invalid amount')
        elif (bills.lower() == 'b'):
            cus_id = input('enter customer account ID:')
            cus_amount = input('enter amount to pay:')
            print('you have successfully pay',cus_amount,'electricity bill for ID',cus_id)
        else:
            print('invalid selection')
        restart = input('would you like to go back? ')
        if restart in('y','YES','yes','Y'):
            print('thank you')
        else:
            print('pls select a valid option')
    elif (atm_menu.lower() == 'd'):
        bank = input('enter customer bank name: ')
        account_num = int(input('enter customer account number: '))
        amount = int(input('enter amount: '))
        print(amount,'has been transfared to',account_num)
        restart = input('would you like to go back? ')
        if restart in('y','YES','yes','Y'):
            print('thank you')
        else:
            print('pls select a valid option')
    else:
        print('invalid selection')
        restart = input('would you like to go back? ')
        if restart in('y','YES','yes','Y'):
            print('thank you')
        else:
            print('pls select a valid option')
elif cus_pin != ('1234'): 
     print('incorect password')
     chance = chance-1
     print("Card not available")
            
    
    
        
