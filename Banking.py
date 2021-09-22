keepgoing0 = True
keepgoing1 = True
keepgoing2 = True
keepgoing3 = True
keepgoing4 = True
keepgoing5 = True
correct = False
balance = 0
import time, datetime

class Transaction:
    def __init__(self,action,fAmount,timestamp):
        self.action = action
        self.fAmount = fAmount
        self.timestamp = timestamp
        
class Transaction_History:
    def __init__(self):
        self.TransHistory = []
    def Add_Transaction (self,t):
        self.TransHistory.append (t)

def GetDataFromLine(line):
    elems = line.split(",")
    return elems[1]

# class Record ?? Specify the path of the program 
def RecordSaveNew(AccountName, AccountId, Record, Balance, t_history):
    with open(str(account_id) + ".txt", "w") as my_file:
        print ("==== INFO", file=my_file)
        print ("NAME," + account_name, file=my_file)
        print ("ID," + account_id, file=my_file)
        record_list = record.split(",")
        #print ("EMAIL," + record[0], file=my_file)
        #print ("PHONE," + record[1], file=my_file)
        #print ("PREF," + record[2], file=my_file)
        #print ("Q1," + record[3], file=my_file)
        #print ("Q2," + record[4], file=my_file)
        #print ("Q3," + record[5], file=my_file)
        #print ("==== Balance", file=my_file)
        print ("BALANCE," + str(balance), file=my_file)
        print ("==== Transactions", file=my_file)
        for transaction in t_history:
            data = [transaction.action, str(transaction.fAmount), transaction.timestamp]
            print(",".join(data), file=my_file)

def RecordRead(account_id, t_history):
    with open(str(account_id) + ".txt", "r") as my_file:
        print(my_file.readline())
        name_line = my_file.readline().strip()
        print("name line:", name_line)
        account_name = GetDataFromLine(name_line)
        account_id = GetDataFromLine(my_file.readline ().strip ())
        #record = GetDataFromLine(my_file.readline ().strip ())
        #record += "," + GetDataFromLine(my_file.readline ().strip ())
        #record += "," + GetDataFromLine(my_file.readline ().strip ())
        my_file.readline()
        balance = GetDataFromLine(my_file.readline ().strip ())
        my_file.readline()
        for line in my_file:
            data = line.split(",") 
            #history = my_file.readline ().strip ()
            transaction = Transaction(data[0], round(float(data[1]), 2), data[2])
            t_history.Add_Transaction(transaction)

    #print([account_name, account_id, record, balance, history])

    return account_name, account_id, record, balance

def RecordUpdate():
    pass


history = Transaction_History()
record = ""

#end of Defining Stuff

print ("Welcome to Mission Code Name Chocolate Bar")
print ("This is the Faux Bank program")
print ("Thank you for contacting the Faux Bank!")

#end of Bank Welcome

while keepgoing0 == True:
    print ("\nPlease respond with either 'E' or 'N'")
    account = input ("\tDo you have an Existing Account (E) or do you want to make a New Account (N)? ")
    account = account.strip().upper()
    if account == "E":
        account_id = input ("\t\tAccount ID: ")
        #[account_name, account_id, record, balance] = RecordRead(account_id, history)
        keepgoing0 = False
        
    elif account == "N":
        print ("\nPlease make an Account Name")
        account_name = input ("\tAccount Name: ")
        print ("\nPlease make an Account ID that you'll be able to remember (Numbers only please)")
        print ("You'll be using your Account ID to Login to your bank account every time, so treat it like a password")
        account_id = input ("\tAccount ID: ")
        keepgoing0 = False
        balance = 0
    else:
        print ("\nInvalid Entry, please try again")
        keepgoing0 = True
    
#end of Account

print ("\n\t\tWelcome " + account_name + "!")

#end of Personal Welcome

while keepgoing1 == True:
    print ("\nWelcome to the main menu")
    print ("\n\tSelect Option A to Contact an Agent")
    print ("\tSelect Option B to find Bank Hours and Locations")
    print ("\tSelect Option C to Deposit, Withdraw, or make a Balance Inquiry")
    print ("\tSelect Option D to View Transactions")
    print ("\tSelect Option E to Quit")
    print ("\n\tPlease select an option (A-D) to proceed (Enter A, B, C, D, or E [All Caps])")
    Mm1 = input ("\nSelect Option to Continue: ")
    Mm1 = Mm1.strip().upper()

#end of Main Menu 1
    
    if Mm1 == "A":
        print ("\n\tPlease state your name, account email, and phone number.")
        name = input ("\t\tName: ")
        record = record + "\n" + name + "\n"
        email = input ("\t\tAccount Email: ")
        record = record + email + "\n"
        phone = input ("\t\tPhone Number: ")
        record = record + phone + "\n"
        print ("\tState what way you prefer for us to get back to you.")
        correct = False
        while correct == False:
            contact = input ("\t\tEmail or Phone Number: ")
            contact = contact.strip().upper()
            record = record + "\n" + contact + "\n"
            if contact == "EMAIL":
                print ("\tWe also ask you to tell us your question(s) so that when we contact you we can be of immediate service.")
                print ("\tWe apologize deeply, but due to technical limitations, a maximum of 3 questions is allowed.")
                print ("\tIf you have more questions, you can contact us directly, or submit another question form.")
                print ("\t\t(This is a question form.)")
                print ("\tOur agents will answer all your questions at once, however, if you have filled in more than one question form.")
                print ("\tIf you have less than one question, just leave the other question lines blank, and move on.")
                print ("\tWe appreciate your understanding!")
                print ("\tOnce you are done, the system will automatically redirect you to the main menu.")
                question1 = input ("\t\tQuestion 1: ")
                record = record +"\n" + question1 + "\n"
                question2 = input ("\t\tQuestion 2: ")
                record = record + question2 + "\n"
                question3 = input ("\t\tQuestion 3: ")
                record = record + question3 + "\n"
                correct = True
            elif contact == "PHONE NUMBER":
                print ("\tWe also ask you to tell us your question(s) so that when we contact you we can be of immediate service.")
                print ("\tWe apologize deeply, but due to technical limitations, a maximum of 3 questions is allowed.")
                print ("\tIf you have more questions, you can contact us directly, or submit another question form.")
                print ("\t\t(This is a question form.")
                print ("\tOur agents will answer all your questions at once, however, if you have filled in more than one question form.")
                print ("\tIf you have less than one question, just leave the other question lines blank, and move on.")
                print ("\tWe appreciate your understanding!")
                print ("\tOnce you are done, the system will automatically redirect you to the main menu.")
                question1 = input ("\t\tQuestion 1: ")
                record = record + question1 + "\n"
                question2 = input ("\t\tQuestion 2: ")
                record = record + question2 + "\n"
                question3 = input ("\t\tQuestion 3: ")
                record = record + question3 + "\n"
                correct = True
            else:
                print ("Invalid Entry, please try again")
                correct = False

#end of Contact an Agent

    elif Mm1 == "B":
        print ("\n-----------------------------------------------------------------------------------------------------------------")
        print ("\n\tThe Faux Bank is open daily, from 6am - 10pm, while the atm is open 24/7.")
        print ("\tCertain holidays are exceptions")
        print ("\tPlease check our website (www.fauxbank.com) on the holiday for more details.")
        print ("\tThe Faux Bank can be found throughout Minnesota, in Hopkins, Minnetonka, Minneapolis, and Eden Prarie.")
        print ("\tThe new location in Edina is coming soon.")
        print ("\n-----------------------------------------------------------------------------------------------------------------")
        confirm = input ("\nPress Enter to return to the previous menu")

#end of Bank Hours and Locations

    elif Mm1 == "C":
        keepgoing2 = True        
        while keepgoing2 == True:
            print ("\n\tSelect Option 1 to Deposit an action into your account")
            print ("\tSelect Option 2 to Withdraw an action from your account")
            print ("\tSelect Option 3 to make a Balance Inquiry")
            print ("\tSelect Option 4 to go back to the Main Menu")
            print ("\tSelect Option 5 to Exit")
            print ("\n\tPlease select an option (1-5) to proceed (Enter 1, 2, 3, 4, or 5)")
            Mm2 = input ("\nSelect Option to Continue: ")
            Mm2 = Mm2.strip().upper()

#end of Main Menu 2

            if Mm2 == "1":
                keepgoing3 = True
                while keepgoing3 == True:
                    fAmount = round (float (input ("\n\tState the action you wish to Deposit: ")), 2)
                    print ("\nPlease confirm the transaction by typing in: 'Y' or 'Yes'")
                    print ("If you wish to change your transaction action or action, type 'N' or 'No'")
                    keepgoing4 = True
                    while keepgoing4 == True:
                        Sm1 = input ("\n\tAre you sure you wish to deposit $ " + str(fAmount) + " into your account? ")
                        Sm1 = Sm1.strip().upper()
                        if Sm1 == "YES" or Sm1 == "Y":
                            print ("\n\tTransaction confirmed.")
                            balance = balance + fAmount
                            t1 = Transaction("Deposit", fAmount, str(datetime.datetime.now()))
                            history.Add_Transaction(t1)
                            print ("\n\tTransaction completed.")
                            keepgoing0 = False
                            keepgoing1 = False
                            keepgoing2 = True
                            keepgoing3 = False
                            keepgoing4 = False
                            keepgoing5 = False
                        elif Sm1 == "NO" or Sm1 == "N":
                            keepgoing5 = True
                            while keepgoing5 == True:
                                Sm2 = input ("\nWhat do you wish to change? Amount or Action? ")
                                Sm2 = Sm2.strip().upper()
                                if Sm2 == "Amount":
                                    keepgoing0 = False
                                    keepgoing1 = False
                                    keepgoing2 = False
                                    keepgoing3 = True
                                    keepgoing4 = False
                                    keepgoing5 = False
                                elif Sm2 == "Action":
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
                    fAmount = round (float (input ("\n\tState the amount you wish to Withdraw: ")), 2)
                    print ("\nPlease confirm the transaction by typing in: 'Y' or 'Yes'")
                    print ("If you wish to change your transaction amount or action, type 'N' or 'No'")
                    keepgoing4 = True
                    while keepgoing4 == True:
                        Sm1 = input ("\n\tAre you sure you wish to withdraw $ " + str(fAmount) + " from your account? ")
                        Sm1 = Sm1.strip().upper()
                        if Sm1 == "YES" or Sm1 == "Y":
                            print ("\n\tTransaction confirmed.")
                            balance = balance - fAmount
                            t2 = Transaction("Withdrawal", fAmount, str(datetime.datetime.now()))
                            history.Add_Transaction(t2)
                            print ("\n\tTransaction completed.")
                            keepgoing0 = False
                            keepgoing1 = False
                            keepgoing2 = True
                            keepgoing3 = False
                            keepgoing4 = False
                            keepgoing5 = False
                        elif Sm1 == "NO" or Sm1 == "N":
                            keepgoing5 = True
                            while keepgoing5 == True:
                                Sm2 = input ("\nWhat do you wish to change? Amount or Action? ")
                                Sm2 = Sm2.strip().upper()
                                if Sm2 == "Amount":
                                    keepgoing0 = False
                                    keepgoing1 = False
                                    keepgoing2 = False
                                    keepgoing3 = True
                                    keepgoing4 = False
                                    keepgoing5 = False
                                elif Sm2 == "Action":
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
                print ("\n-----------------------------------------------------------------------------------------------------------------")
                print ("\n\tYou have $ " + str (balance) + " in your account.")
                print ("\n-----------------------------------------------------------------------------------------------------------------")
                confirm = input ("\nPress Enter to return to the previous menu")
                keepgoing0 = False
                keepgoing1 = False
                keepgoing2 = True
                keepgoing3 = False
                keepgoing4 = False
                keepgoing5 = False

#end of Balance Inquiry
                
            elif Mm2 == "4":
                keepgoing0 = False
                keepgoing1 = True
                keepgoing2 = False
                keepgoing3 = False
                keepgoing4 = False
                keepgoing5 = False
                
#end of Return to Main Menu 1

            elif Mm2 == "5":
                print ("\n\tHave a great day!")
                print ("\tThanks for contacting the Faux Bank!")
                print ("\tCall us at: (123)-456-7890 if you have any questions.")
                print ("\tVisit our website at www.fauxbank.com for more contact information and information about us.")
                print ("\tPlease be forewarned that our agents may or may not be available at the time.")
                print ("\tIf you have any unanswered questions, please go to 'Contact an Agent'")
                print ("\tThere, you can leave your contact info and question(s), and we'll get back to you as soon as we can.")
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
        print ("\n-----------------------------------------------------------------------------------------------------------------")
        for transaction in history.TransHistory:
            print ("\n\t%10s: $%10.2f at %s"%(transaction.action, transaction.fAmount, transaction.timestamp))
        print ("\n-----------------------------------------------------------------------------------------------------------------")
        confirm = input ("\nPress Enter to return to the previous menu")

#end of Transaction History

    elif Mm1 == "E":
        print ("\n\tHave a great day!")
        print ("\tThanks for contacting the Faux Bank!")
        print ("\tCall us at: (123)-456-7890 if you have any questions.")
        print ("\tVisit our website at www.fauxbank.com for more contact information and information about us.")
        print ("\tPlease be forewarned that our agents may or may not be available at the time.")
        print ("\tIf you have any unanswered questions, please go to 'Contact an Agent'")
        print ("\tThere, you can leave your contact info and question(s), and we'll get back to you as soon as we can.")
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

#RecordSaveNew(account_name, account_id, record, balance, history)

