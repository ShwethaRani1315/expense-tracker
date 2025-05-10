print("Hello! Welcome to Personal Expense Tracker!")

userExpenses = {}

contMenu = True

#Essential Functions

def printMenu():
    print("MAIN MENU")
    print("----------")
    print("1. Add Expense")
    print("2. View Total Expenses")
    print("3. View Daily Summary")
    print("4. View Category Summary")
    print("5. Exit")

def updateUserAction():
    try:
        return int(input("\nPlease enter the action you'd like to perform: "))
    
    except ValueError:
        print("\nInvalid input! Please enter a number from 1 to 5")
        return 0

def addExpense():
    print("\n------------")
    print("ADD EXPENSE")
    print("------------")

    #Get details of the expense
    print("Please enter the details of the expense as follows: ")
    date = input("Date (yyyy-mm-dd): ")
    category = input("Category: ")
    amount = int(input("Amount: "))
    
    #If there is no entry for the given date, create a new empty entry
    if date not in userExpenses:
        userExpenses[date] = []
    
    #Append the expense details to the corresponding date
    userExpenses[date].append((category, amount))

    print("Expense data successfully added!\n")


def viewTotalExpenses():
    print("\n--------------------")
    print("VIEW TOTAL EXPENSES")
    print("--------------------")

    #Get the corresponding date from the user
    userDate = input("Enter the date of interest: ")
    print("\n")

    #If expense entry found in userDate, calculate total expenses
    if userDate in userExpenses:
        totalExpense = 0

        for category, amount in userExpenses[userDate]:
            print(f"{category} : {amount}")
            totalExpense += amount

        print("------------------------------")
        print("Total Expense: ", totalExpense)
        print("------------------------------")

    else:
        print("No data found for the given date!")



def viewDailySummary():
    print("\n-------------------")
    print("VIEW DAILY SUMMARY")
    print("-------------------")

    if not userExpenses:
        print("Sorry! No Expense data found!")
        return

    for userDate, expenses in sorted(userExpenses.items()):
        print(f"Date: {userDate}")
        print("------------------")
        dailyTotal = 0
        
        for category, expense in expenses:
            print(f"{category} : Rs.{expense}")
            dailyTotal += expense
        
        print("-------------------")
        print(f"Total: Rs.{dailyTotal}\n")

def viewCategorySummary():
    print("\n----------------------")
    print("VIEW CATEGORY SUMMARY")
    print("----------------------")

    if not userExpenses:
        print("Sorry! No Expense Data Found!")
        return
    
    #Empty dictionary to hold all categories and corresponding totals
    categoryTotals = {}

    for expense in userExpenses.values():
        for category, expense in expense:

            #Assign initial category total to 0
            if category not in categoryTotals:
                categoryTotals[category] = 0

            categoryTotals[category] += expense
        
        print(f"{categoryTotals}")

        for category, total in categoryTotals.items():
            print(f"{category}: Rs.{total}")
        


#Keep the program running until the user chooses exit
while contMenu == True:
    printMenu()
    userAction = updateUserAction()

    if userAction == 1:
        addExpense()
    
    elif userAction == 2:
        viewTotalExpenses()
    
    elif userAction == 3:
        viewDailySummary()
    
    elif userAction == 4:
        viewCategorySummary()
    
    elif userAction == 5:
        print("\nThank you for using the Expense Tracker!")
        print("Exiting...")
        break

    cont = input("\nDo you want to continue? (y/n)").strip().lower()

    if cont != 'y':
        print("Thank you for using our Expense Tracker!")
        print("Exiting...")
        contMenu = False

    

