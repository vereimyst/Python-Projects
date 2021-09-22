keepgoing0 = True
keepgoing1 = True
keepgoing2 = True
keepgoing3 = True
keepgoing4 = True
keepgoing5 = True
correct = False
balance = 0
import time

class Transaction:
    def __init__(self,type,amount,timestamp):
        self.type = type
        self.amount = fAmount
        self.timestamp = timestamp

class Transaction_History:
    def __init__(self):
        self.TransHistory = []
    def Add_Transaction (self,t):
        self.TransHistory.append (t)

history = Transaction_History()
record = ""

#end of Defining Stuff

print ("Welcome to Mission Code Name Chocolate Bar")
time.sleep (1)
print ("This is the Faux Bank program")
time.sleep (2)
print ("Thank you for contacting the Faux Bank!")
time.sleep (1)
print ("Please follow the instructions given EXACTLY. Thanks!!")

#end of Bank Welcome

while keepgoing0 == True:
    time.sleep (2)
    print ("\nPlease respond with either 'Existing' or 'New'")
    time.sleep (1)
    account = input ("\tDo you have an Existing Account or do you want to make a New Account? ")
    if account == "Existing":
        account_id = input ("\t\tAccount ID: ")
        with open(str(account_id) + ".txt", "r") as my_file:
            account_name = my_file.readline ().strip ()
            account_id = my_file.readline ().strip ()
        keepgoing0 = False
        
    elif account == "New":
        print ("\nPlease make an Account Name")
        time.sleep (1)
        account_name = input ("\tAccount Name: ")
        print ("\nPlease make an Account ID that you'll be able to remember")
        time.sleep (1)
        print ("You'll be using your Account ID to Login to your bank account every time, so treat it like a password")
        time.sleep (1)
        account_id = input ("\tAccount ID: ")
        keepgoing0 = False

    else:
        print ("\nInvalid Entry, please try again")
        keepgoing0 = True
    
#end of Account

print ("\n\t\tWelcome " + account_name + "!")

#end of Personal Welcome

while keepgoing1 == True:
    time.sleep (2)
    print ("\nWelcome to the main menu")
    time.sleep (1)
    print ("\n\tSelect Option A to Contact an Agent")
    time.sleep (1)
    print ("\tSelect Option B to find Bank Hours and Locations")
    time.sleep (1)
    print ("\tSelect Option C to Deposit, Withdraw, or make a Balance Inquiry")
    time.sleep (1)
    print ("\tSelect Option D to View Transactions")
    time.sleep (1)
    print ("\tSelect Option E to Quit")
    time.sleep (1)
    print ("\n\tPlease select an option (A-D) to proceed (Enter A, B, C, D, or E [All Caps])")
    time.sleep (1)
    Mm1 = input ("\nSelect Option to Continue: ")

#end of Main Menu 1
    
    if Mm1 == "A":
        time.sleep (1)
        print ("\nRedirecting you to 'Contacting an Agent'...")
        time.sleep (2)
        print ("\n\tPlease state your name, account email, and phone number.")
        time.sleep (1)
        name = input ("\t\tName: ")
        record = record + "\n" + name + "\n"
        email = input ("\t\tAccount Email: ")
        record = record + email + "\n"
        phone = input ("\t\tPhone Number: ")
        record = record + phone + "\n"
        time.sleep (1)
        print ("\tState what way you prefer for us to get back to you.")
        correct = False
        while correct == False:
            contact = input ("\t\tEmail or Phone Number: ")
            record = record + "\n" + contact + "\n"
            if contact == "Email":
                time.sleep (1)
                print ("\tWe also ask you to tell us your question(s) so that when we contact you we can be of immediate service.")
                time.sleep (1)
                print ("\tWe apologize deeply, but due to technical limitations, a maximum of 3 questions is allowed.")
                time.sleep (1)
                print ("\tIf you have more questions, you can contact us directly, or submit another question form.")
                print ("\t\t(This is a question form.)")
                time.sleep (1)
                print ("\tOur agents will answer all your questions at once, however, if you have filled in more than one question form.")
                time.sleep (1)
                print ("\tIf you have less than one question, just leave the other question lines blank, and move on.")
                time.sleep (1)
                print ("\tWe appreciate your understanding!")
                time.sleep (1)
                print ("\tOnce you are done, the system will automatically redirect you to the main menu.")
                time.sleep (1)
                question1 = input ("\t\tQuestion 1: ")
                record = record +"\n" + question1 + "\n"
                question2 = input ("\t\tQuestion 2: ")
                record = record + question2 + "\n"
                question3 = input ("\t\tQuestion 3: ")
                record = record + question3 + "\n"
                time.sleep (3)
                print ("\nRedirecting you to the main menu...")
                time.sleep (2)
                correct = True
            elif contact == "Phone Number":
                time.sleep (1)
                print ("\tWe also ask you to tell us your question(s) so that when we contact you we can be of immediate service.")
                time.sleep (1)
                print ("\tWe apologize deeply, but due to technical limitations, a maximum of 3 questions is allowed.")
                time.sleep (1)
                print ("\tIf you have more questions, you can contact us directly, or submit another question form.")
                print ("\t\t(This is a question form.")
                time.sleep (1)
                print ("\tOur agents will answer all your questions at once, however, if you have filled in more than one question form.")
                time.sleep (1)
                print ("\tIf you have less than one question, just leave the other question lines blank, and move on.")
                time.sleep (1)
                print ("\tWe appreciate your understanding!")
                time.sleep (1)
                print ("\tOnce you are done, the system will automatically redirect you to the main menu.")
                time.sleep (1)
                question1 = input ("\t\tQuestion 1: ")
                record = record + question1 + "\n"
                question2 = input ("\t\tQuestion 2: ")
                record = record + question2 + "\n"
                question3 = input ("\t\tQuestion 3: ")
                record = record + question3 + "\n"
                time.sleep (3)
                print ("\nRedirecting you to the main menu...")
                time.sleep (2)
                correct = True
            else:
                print ("Invalid Entry, please try again")
                correct = False

#end of Contact an Agent

    elif Mm1 == "B":
        time.sleep (1)
        print ("\nRedirecting you to 'Bank Hours and Locations'...")
        time.sleep (2)
        print ("\n\tThe Faux Bank is open daily, from 6am - 10pm, while the atm is open 24/7.")
        time.sleep (1)
        print ("\tCertain holidays are exceptions")
        time.sleep (1)
        print ("\tPlease check our website (www.fauxbank.com) on the holiday for more details.")
        time.sleep (1)
        print ("\tThe Faux Bank can be found throughout Minnesota, in Hopkins, Minnetonka, Minneapolis, and Eden Prarie.")
        time.sleep (1)
        print ("\tThe new location in Edina is coming soon.")
        time.sleep (3)
        print ("\nRedirecting you to the main menu...")

#end of Bank Hours and Locations

    elif Mm1 == "C":
        keepgoing2 = True        
        while keepgoing2 == True:
            time.sleep (1)
            print ("\nRedirecting you to 'Deposit, Withdraw, & Balance Inquiry'")
            time.sleep (2)
            print ("\n\tSelect Option 1 to Deposit an amount into your account")
            time.sleep (1)
            print ("\tSelect Option 2 to Withdraw an amount from your account")
            time.sleep (1)
            print ("\tSelect Option 3 to make a Balance Inquiry")
            time.sleep (1)
            print ("\tSelect Option 4 to go back to the Main Menu")
            time.sleep (1)
            print ("\tSelect Option 5 to Exit")
            time.sleep (1)
            print ("\n\tPlease select an option (1-5) to proceed (Enter 1, 2, 3, 4, or 5)")
            time.sleep (1)
            Mm2 = input ("\nSelect Option to Continue: ")

#end of Main Menu 2

            if Mm2 == "1":
                keepgoing3 = True
                while keepgoing3 == True:
                    print ("\nRedirecting you to Deposit...")
                    time.sleep (2)
                    fAmount = input("\n\tState the amount you wish to Deposit: ")
                    time.sleep (1)
                    print ("\nPlease confirm the transaction by typing in: 'Y' or 'Yes'")
                    time.sleep (1)
                    print ("If you wish to change your transaction amount or action, type 'N' or 'No'")
                    keepgoing4 = True
                    while keepgoing4 == True:
                        time.sleep (1)
                        Sm1 = input ("\n\tAre you sure you wish to deposit $ " + str(fAmount) + " into your account? ")
                        if Sm1 == "Yes" or Sm1 == "Y":
                            time.sleep (1)
                            print ("\n\tTransaction confirmed.")
                            time.sleep (2)
                            print ("\n\tLoading...")
                            time.sleep (4)
                            balance = balance + int (fAmount)
                            t1 = Transaction("Deposit", fAmount, "6/6/17-12:45")
                            history.Add_Transaction(t1)
                            print ("\n\tTransaction completed.")
                            keepgoing0 = False
                            keepgoing1 = False
                            keepgoing2 = True
                            keepgoing3 = False
                            keepgoing4 = False
                            keepgoing5 = False
                        elif Sm1 == "No" or Sm1 == "N":
                            keepgoing5 = True
                            while keepgoing5 == True:
                                Sm2 = input ("\nWhat do you wish to change? Amount or Action? ")
                                if Sm2 == "Amount":
                                    time.sleep (1)
                                    print ("\nPlease wait as we bring you back to Deposit...")
                                    time.sleep (2)
                                    keepgoing0 = False
                                    keepgoing1 = False
                                    keepgoing2 = False
                                    keepgoing3 = True
                                    keepgoing4 = False
                                    keepgoing5 = False
                                elif Sm2 == "Action":
                                    time.sleep (1)
                                    print ("\nPlease wait as we bring you back to the DWB main menu...")
                                    time.sleep (2)
                                    keepgoing0 = False
                                    keepgoing1 = False
                                    keepgoing2 = True
                                    keepgoing3 = False
                                    keepgoing4 = False
                                    keepgoing5 = False
                                else:
                                    print ("\nInvalid Entry, please try again.")
                                    keepgoing0 = False
                                    keepgoing1 = False
                                    keepgoing2 = False
                                    keepgoing3 = False
                                    keepgoing4 = False
                                    keepgoing5 = True                                   
                        else:
                            print ("\nInvalid Entry, please try again.")
                            keepgoing0 = False
                            keepgoing1 = False
                            keepgoing2 = False
                            keepgoing3 = False
                            keepgoing4 = True
                            keepgoing5 = False

#end of Deposit
                            
            elif Mm2 == "2":
                keepgoing3 = True
                while keepgoing3 == True:
                    print ("\nRedirecting you to Withdraw...")
                    time.sleep (2)
                    fAmount = input("\n\tState the amount you wish to Withdraw: ")
                    time.sleep (1)
                    print ("\nPlease confirm the transaction by typing in: 'Y' or 'Yes'")
                    time.sleep (1)
                    print ("If you wish to change your transaction amount or action, type 'N' or 'No'")
                    keepgoing4 = True
                    while keepgoing4 == True:
                        time.sleep (1)
                        Sm1 = input ("\n\tAre you sure you wish to withdraw $ " + str(fAmount) + " from your account? ")
                        if Sm1 == "Yes" or Sm1 == "Y":
                            time.sleep (1)
                            print ("\n\tTransaction confirmed.")
                            time.sleep (2)
                            print ("\n\tLoading...")
                            time.sleep (4)
                            balance = balance - int (fAmount)
                            t2 = Transaction("Withdrawal", fAmount, "6/6/17-12:45")
                            history.Add_Transaction(t2)
                            print ("\n\tTransaction completed.")
                            keepgoing0 = False
                            keepgoing1 = False
                            keepgoing2 = True
                            keepgoing3 = False
                            keepgoing4 = False
                            keepgoing5 = False
                        elif Sm1 == "No" or Sm1 == "N":
                            keepgoing5 = True
                            while keepgoing5 == True:
                                Sm2 = input ("\nWhat do you wish to change? Amount or Action? ")
                                if Sm2 == "Amount":
                                    time.sleep (1)
                                    print ("\nPlease wait as we bring you back to Withdraw...")
                                    time.sleep (2)
                                    keepgoing0 = False
                                    keepgoing1 = False
                                    keepgoing2 = False
                                    keepgoing3 = True
                                    keepgoing4 = False
                                    keepgoing5 = False
                                elif Sm2 == "Action":
                                    time.sleep (1)
                                    print ("\nPlease wait as we bring you back to the DWB main menu...")
                                    time.sleep (2)
                                    keepgoing0 = False
                                    keepgoing1 = False
                                    keepgoing2 = True
                                    keepgoing3 = False
                                    keepgoing4 = False
                                    keepgoing5 = False
                                else:
                                    print ("\nInvalid Entry, please try again.")
                                    keepgoing0 = False
                                    keepgoing1 = False
                                    keepgoing2 = False
                                    keepgoing3 = False
                                    keepgoing4 = False
                                    keepgoing5 = True                                   
                        else:
                            print ("\nInvalid Entry, please try again.")
                            keepgoing0 = False
                            keepgoing1 = False
                            keepgoing2 = False
                            keepgoing3 = False
                            keepgoing4 = True
                            keepgoing5 = False

#end of Withdrawal
                            
            elif Mm2 == "3":
                time.sleep (1)
                print ("\nRedirecting you to Balance Inquiry...")
                time.sleep (2)
                print ("\n\tYou have $ " + str (balance) + " in your account.")
                time.sleep (3)
                print ("\nPlease wait as we bring you back to the DWB main menu...")
                time.sleep (2)
                keepgoing0 = False
                keepgoing1 = False
                keepgoing2 = True
                keepgoing3 = False
                keepgoing4 = False
                keepgoing5 = False

#end of Balance Inquiry
                
            elif Mm2 == "4":
                print ("\nRedirecting you to the Main Menu...")
                keepgoing0 = False
                keepgoing1 = True
                keepgoing2 = False
                keepgoing3 = False
                keepgoing4 = False
                keepgoing5 = False
                
#end of Return to Main Menu 1

            elif Mm2 == "5":
                print ("\nRedirecting you to the exit...")
                time.sleep (2)
                print ("\n\tHave a great day!")
                time.sleep (1)
                print ("\tThanks for contacting the Faux Bank!")
                time.sleep (1)
                print ("\tCall us at: (123)-456-7890 if you have any questions.")
                time.sleep (1)
                print ("\tVisit our website at www.fauxbank.com for more contact information and information about us.")
                time.sleep (1)
                print ("\tPlease be forewarned that our agents may or may not be available at the time.")
                time.sleep (1)
                print ("\tIf you have any unanswered questions, please go to 'Contact an Agent'")
                time.sleep (1)
                print ("\tThere, you can leave your contact info and question(s), and we'll get back to you as soon as we can.")
                time.sleep (1)
                print ("\tWe hope this has been of service!")
                keepgoing0 = False
                keepgoing1 = False
                keepgoing2 = False
                keepgoing3 = False
                keepgoing4 = False
                keepgoing5 = False

#end of Exit (Mm2)
            
            else:
                print ("\nInvalid Entry, please try again.")
                keepgoing0 = False
                keepgoing1 = False
                keepgoing2 = True
                keepgoing3 = False
                keepgoing4 = False
                keepgoing5 = False

#end of Invalid Entry (Mm2)


    elif Mm1 == "D":
        print ("\nRedirecting you to 'Transaction History'...")
        time.sleep (2)
        print ("\n" + str(history.TransHistory))
        for transaction in history.TransHistory:
            transaction.type
            transaction.fAmount
            transaction.timestamp
        time.sleep (3)
        print ("Automatically bringing you back to the Main Menu...")
        time.sleep (2)
        print ("Redirecting you to the Main Menu...")

#end of Transaction History

    elif Mm1 == "E":
        print ("\nRedirecting you to the exit...")
        time.sleep (2)
        print ("\n\tHave a great day!")
        time.sleep (1)
        print ("\tThanks for contacting the Faux Bank!")
        time.sleep (1)
        print ("\tCall us at: (123)-456-7890 if you have any questions.")
        time.sleep (1)
        print ("\tVisit our website at www.fauxbank.com for more contact information and information about us.")
        time.sleep (1)
        print ("\tPlease be forewarned that our agents may or may not be available at the time.")
        time.sleep (1)
        print ("\tIf you have any unanswered questions, please go to 'Contact an Agent'")
        time.sleep (1)
        print ("\tThere, you can leave your contact info and question(s), and we'll get back to you as soon as we can.")
        time.sleep (1)
        print ("\tWe hope this has been of service!")
        keepgoing0 = False
        keepgoing1 = False
        keepgoing2 = False
        keepgoing3 = False
        keepgoing4 = False
        keepgoing5 = False

#end of Exit (Mm1)

    else:
        print ("\nInvalid Entry, please try again.")
        keepgoing0 = False
        keepgoing1 = True
        keepgoing2 = False
        keepgoing3 = False
        keepgoing4 = False
        keepgoing5 = False

#end of Invalid Entry (Mm1)

with open(str(account_id) + ".txt", "w") as my_file:
    print (account_name, file=my_file)
    print (account_id, file=my_file)
    print (record, file=my_file)    










