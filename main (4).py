#Name: Aamna
#Date: December 12, 2022
#Banking Problem

#import random module so that code will be able to generate random digits
import random

#When called upon the 'balance' will be random numbers from between a thousand and ten thousand
balance = random.randint(1000,10000)

#Introduce the bank and give the user options to choose from.
print("Welcome to the bank of Aamna!")
while True:
  print()
  print("a - Open a new account")
  print("w - Money Withdrawl ")
  print("d - Deposit")
  print("t - Transfer of Funds")
  print("c - Create a credit card ")
  print("q- To Quit/Exit")
  print()
  print()

  #Ask the user which option they choose. Make the information lowercase so that it is easier to make conditions
  user_choice = input("Please choose an option from above to proceed: ").lower()

  # If the user want to open a new account ask them some personal information like their age, name, and postal code
  if user_choice == "a":
    print()
    print("To open a new account please enter the following information")
    user_name=input("Full name: ").capitalize
    user_postal_code = input("Postal Code: ")
    user_age=int(input("Age: "))
    #If the user is older than or are 16 then allow them to open a new account and provide them with their bank number
    if user_age>=16:
      #print their bank number by generating random 6 digit numbers
      print("Your bank number is: " + str(random.randint(100000, 1000000)))
      #Ask user for their phone number
      phone  = input("Please enter your phone number (DIGITS ONLY): ")
      #Make sure that the phone number is valid, as in its 10 digits long. If it is then cingragulate them for opening an account
      if len(phone) == 10:
        print()
        print("Congratulations you have opened a bank account! Your banking information has been sent to your number Thank you! ")      #If the length of the number is less than 10 digits then its invalid and the user needs to try again
      elif len(phone) != 10:
        print("Please type your phone numner (DIGITS ONLY) with no spaces in between")
    #If the user age is less than 16 then tell them that they are too young to open a bank account   
    elif user_age<16:
      print()
      print("Sorry you need to be atleast 16 years old to open a bank account")
  #if the user choses d then they want to deposit money, ask them how much they would like to deposit and add it to their bank account which is the variable 'balance'     
  elif user_choice == "d":
    #Ask for their bank account number 
    account= input("Please enter your 6 digit bank account number to proceed: ")
    #Make sure that its a calid number by checking that it is 6 digits
    if len(account) == 6:
      balance1 = balance
      #print their current balance
      print("Your account balance is: $" + str(balance))
      #Ask the user how much they would like to deposit 
      amount = float(input("Enter amount to be deposited: "))
      #Create an equation that adds teh rpevious balance with money deposited
      balance2 = balance1 + amount
      print()
      #Print their new balance
      print("Your new balance is: $" + str(balance2))
      #Thank the user coming to our bank
      print("Thank you for banking with us!")
    #If the account number is not 6 digits its invalid. tell the user that. 
    elif len(account) != 6:
      print("Incorrect number entered, it needs to be 6 digits")
  #If the user chooses w then they want to withdraw money.  
  elif user_choice == "w":
    #Ask the user their account number 
    account= input("Please enter your 6 digit bank account number to proceed: ")
    #CHeck to make sure that it is 6 digits, meaning a valid account number
    if len(account) == 6:
      balance1 = balance
      #print the current balacne by calling for the balance variable that will give it a random number
      print("Your current account balance is: $" + str(balance1))
      #Ask them how much they want to withdraw 
      amount= float(input("Enter amount to be withdrawn ($1000 max.): "))
      #If they enter an amount more than a thousand tell them that they cant withdraw more that. If it is under a thousand then let them proceed
      if amount<1000:
        #Give them their withdrawl 
        print("Here is your withdrawl of: $" + str(amount))
        #Subtract teh amount withdrawn from the balance
        balance1 = balance1 - amount
        print()
        #print thier balance after the withdrawl
        print("Your balance is now " + str(balance1))
        #If the amount is more than a 1000 dollars
      elif amount>1000:
        print("You have entered a withdrawl that exceeds the limit of the $1000 maximum")
    #If account number is not 6 digits then tell them that they entered an invalid bank account number and that they need to try agian
    elif len(account) != 6:
        print("Ivalid bank account number. Please try again")

  #If they choose t then the user wants to tranfer funds. Tell them the process to transfer
  elif user_choice == "t":
    print("To transfer funds")
    #Tell them to enter the 6 digit account from which they want to transfer th emoney 
    account = input("Please enter the 6 digit account from which you would like to take out money: ")
    #Make sure that the account is 6 digits, as in that its valid
    if len(account) == 6:
      balance1 = balance
      #Show them their current balance
      print("Your current account balance is: $" + str(balance1)) 
      #ASk them how much they want to trandfer to a differnt account
      amount= float(input("Enter amount to be transferred ($1000 max.): "))
      #If they enter an amount less than 1000 then its valid so allow them to proceed
      if amount<1000:
        #ASk them to provide the account number that they want to transfer the money to 
        account1 = input("Next enter the 6 digit account that you would like to transfer the $" + str(amount) + " to: ")
        #check if that account is valid, by making sure its 6 digits
        if len(account1) == 6:
          #If the account number is valid then allow them to procceed. Print the information that they have provided 
          print("Your $" + str(amount) + " from the account number " + str(account) + " has been transferred to the account number " + str(account1))
          #In the situation that they enter a bank account number is less than 6 digits its invalud 
        elif len(account1) != 6:
          print("invalid account number please try again")
          #subtract the amount withdrawn with the  balance of the account
        balance1 = balance1 - amount
        print()
        #print their balance after the withdrawl 
        print("Your balance is now " + str(balance1))
        #If they want to transfer more than 1000 tell them that there is limit to how much you can transfer
      elif amount>1000:
        print("You have entered a transfer that exceeds the limit of the $1000 maximum")
        #If the account that they enter is less than 6 digits then its not a valid account number 
    elif len(account) != 6:
        print("Ivalid bank account number. Please try again")
    #if user choses c, they want to create a credit card
  if user_choice == "c":
    #Tell them to enter the following information
    print ("To create a credit card please enter the following information")
    #Ask them for their name
    name = input("Full Name: ")
    #Ask them for their address
    address = input("Address: ")
    #Ask for their sociak slecurity number and make sure that it is the right length
    social_security = input("Social security number: ")
    #If they have entered a valild social security number then allow them to proceed
    if len(social_security) ==  9:
      #Ask them for their age
      user_age = int(input("Age: "))
      #If they are younger than 16 then tell them that they are too young
      if user_age<16:
        print()
        print("Sorry you need to be atleast 16 to create a credit card")
        #If the user if older than 16
      if user_age>=16:
        #Tell them their credit card number 
        print("Your credit card number is: " + str(random.randint(100000000000, 1000000000000)))
        #Tell them their cvc number
        print("Your CVC number is: " + str(random.randint(100, 1000)))
        #Tell the user the expiry date
        print("The expiry date is: 04/09/26")
        print()
        #Tell the user that the card will be emailed to them in a couple of days
        print("Your card will be emailed to your address in around 5-10 business days")
    #If the social security number they enter is invalid then tell them that and also tell them to try again 
    elif social_security != 9:
      print("Invalid social security number, please try again")
    # If the user chooses q then they want to quit, so break the loop and thank them for coming to The Bank of Aamna
  elif user_choice == "q":
    print("Thank you for banking with the bank of Aamna! Have a good day.")
    break 
