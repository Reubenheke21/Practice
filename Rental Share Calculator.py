#What we're going to do is create a simple app that lets you enter either your rent/mortgage, bills etc and will work our how much you should pay pert week/fortnight/Month

mortgage = []

print("Welcome to my app! Here you will be able to find out how much you should be paying for each week/fortnight/month for your bills")
print("What I will do is ask you a couple of quesitons and spit out how much you should be paying")


def start():
    frequency = input("What frequency do you get paid? Weekly/Fornightly/Monthly: ").lower()

    if frequency == "weekly":
        print("You have picked weekly!")
        weekly()
    elif frequency == "fortnightly":
        print("You have picked fortnightly!")
        fortnightly
    elif frequency == "monthly":
        print("You have picked monthly!")
        monthly
    else:
        print("I don't know that command please try again!")
        start()

def weekly():
    print("As you picked weekly I will ask you what frequency your bills come out and we will be able to work out what you should be paying a week for all your household bills")
    frequency_rent = input("Do you pay your rent/mortgage weekly, fortnightly or monthly?: ").lower()
    if frequency_rent == "weekly":
        print("You entered weekly")
        mortgage = input("How much is the rent/mortgage?: ")
        other_bills()
    elif frequency_rent == "fortnightly":
        print("You entered fortnightly")
        fortnight_rent = input("How much is the rent/mortgage?: ")
        mortgage = fortnight_rent / 2
        other_bills()
    elif frequency_rent == "monthly":
        print("You entered monthly")
        month_rent = input("How much is the rent/mortgage?: ")
        mortgage = month_rent / 4
        other_bills()
    else:
        print("I dont recognise that command, try again!")
        weekly()
    

def other_bills():
    other_bills = input("Do you have any other bills? (yes/no) ").lower()

    if other_bills == "yes":
        household_bills()
    elif other_bills == "no":
        total_bill()
    else:
        print("I dont recognise that request please try again!")
        other_bills()
    
def household_bills():
    list_of_bills = []
    list_of_bills = input("What other bills do you have?")

    for i in list_of_bills:
        frequency = input("You said you have", i," what frequency is that paid in?: ").lower()
        print(frequency)

start()