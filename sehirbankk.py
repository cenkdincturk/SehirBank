import time

print "--- Welcome to SEHIR Bank V.0.1 ---"


def loginPortal():
    global currentUser
    global currentUsersMoney
    userName = raw_input("User Name:")
    password = input("Password:")
    if userName == "Ahmet" and password == 1234:
        print "Welcome Ahmet!"
        currentUser = "Ahmet"
        currentUsersMoney = moneyDict[currentUser]
        print (moneyDict[currentUser])

        mainMenu()

    elif userName == "Zeynep" and password == 4321:
        print "Welcome Zeynep!"
        currentUsersMoney = moneyDict[currentUser]

        currentUser = "Zeynep"
        mainMenu()

    else:
        print "please again"

global moneyDict
moneyDict = {"Ahmet": 0, "Zeynep": 0}


def mainMenu():
    print "1. Withdraw Money"
    print "2. Deposit Money"
    print "3. Transfer Money"
    print "4. My Account Information"
    print "5. Logout"
    loop = True
    while loop:
        choice = input("Please enter the number of the service:")

        if choice == 1:
            withdrawMoney = input("Please enter the amount you want to withdraw: ")
            if withdrawMoney > moneyDict[currentUser] :
                print "cekemezsin"
            elif withdrawMoney <= moneyDict[currentUser]:
                print "cekersin"
            moneyDict.update()
            break
        elif choice == 2:
                depositMoney = input("Please enter the amount you want to drop: ")
                depositMoney+moneyDict[currentUser]
                moneyDict.update()
                print moneyDict
                print "TL added to your account"
                print "Going back to main menu..."
                mainMenu()

        elif choice == 3:
                transferMoney = input("Please enter the amount you want to transfer: ")
                if currentUsersMoney < transferMoney:
                    print "Sorry! You don't have enough money to complete this transaction"
                    print "1. Go back to main menu"
                    print  "2. Transfer again"
                    secondMenu = raw_input(">>>>")
                    if secondMenu == 1:
                        mainMenu()
                    elif secondMenu == 2:
                        transferMoney()
                    else:
                        print "Again"

        elif choice == 4:
            print "------- SEHIR Bank -------"
            print "----------------------------"

        elif choice == 5:
            print "Logout"
            moneyDict.update(moneyDict)
            loop = False
        else:
            raw_input("Wrong option selection. Enter any key to try again..")

loginPortal()
