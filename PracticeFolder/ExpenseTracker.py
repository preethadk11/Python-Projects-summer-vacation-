#Expense Tracker
expenses=[]
def load_expense():
    with open("expense.txt","r") as file:
        for line in file:
            line=line.strip()
            data=line.split(",")
            expenses.append({"category":data[0],"amount":int(data[1])})
def save_expense():
    with open("expense.txt","w") as file:
        for expense in expenses:
            category=expense["category"]
            amount=expense["amount"]
            file.write(f'{category},{amount}\n')
def add_expense():
    category=input("Enter category: ")
    while True:
        amount=input("Enter amount: ")
        if amount.isdigit() and int(amount)>0:
            new_expense={"category":category,"amount":int(amount)}
            expenses.append(new_expense)
            break
        else:
            print("The amount must be numeric and positive")
def view_expense():
    if expenses:
        for i in range(len(expenses)):
            print(i+1,end=". ")
            print(*expenses[i].values(),sep=" : ")
    else:
        print("No record found!")
def search_category():
    item=input("Enter category: ")
    flag=False
    for expense in expenses:
        if expense["category"].lower()==item.lower():
            print(expense["category"],":",expense["amount"])
            flag=True
    if not flag:
        print("Category not found")
def delete_expense():
    for i in range(len(expenses)):
        print(f'{i+1}.{expenses[i]["category"]}:{expenses[i]["amount"]}')
    flag=False
    while True:
        number=int(input("Enter expense number to delete: "))
        if number<=len(expenses) and number>0:
            for i in range(len(expenses)):
                if number==i+1:
                    confirm=input("Are you sure?(yes/no): ")
                    if confirm=="yes":
                        del expenses[i]
                        print("Expense deleted successfully!")
                        flag=True
                        break
                    else:
                        print("Expense not deleted")
            if flag:
                break
        else:
            print("Invalid expense number")
def statistics():
    if not expenses:
        print("Record not found!")
        return
    else:
        largest=expenses[0]["amount"]
        smallest=expenses[0]["amount"]
        total=0
        for expense in expenses:
            if expense["amount"]>largest:
                largest=expense["amount"]
            if expense["amount"]<smallest:
                smallest=expense["amount"]
            total+=expense["amount"]
        print(f'Total Expenses: {total}')
        print(f'Highest Expense: {largest}')
        print(f'Lowest Expense: {smallest}')
        print(f'Average Expense: {total/len(expenses):.2f}')
        print(f'Number of records: {len(expenses)}')
def filter_expense():
    while True:
        minimum=input("Enter minimum amount: ")
        if minimum.isdigit():
            minimum=int(minimum)
            for expense in expenses:
                if expense["amount"]>=minimum:
                    print(f'{expense["category"]}:{expense["amount"]}')
            break
        else:
            print("The amount must be digits")
def sort_expense():
    print("1. Low to High\n2. High to Low")
    while True:
        choice=int(input("Enter choice: "))
        if choice==1:
            sorted_expense = sorted(expenses,key=lambda x:x["amount"])
            print()
            for expense in sorted_expense:
                print(f'{expense["category"]}:{expense["amount"]}')
            break
        elif choice==2:
            sorted_expense=sorted(expenses,key=lambda x:x["amount"],reverse=True)
            print()
            for expense in sorted_expense:
                print(f'{expense["category"]}:{expense["amount"]}')
            break
        else:
            print("Invalid choice!")
menu="\t\t====Expense Tracker====\n1. Add Expense\n2. View Expenses\n3. Search Category\n4. Delete Expense\n5. Statistics\n6.Filter Expense\n7.Sort Expense\n8. Exit"
load_expense()
while True:
    print(menu)
    choice=input("Enter your choice: ")
    if choice.isdigit():
        if choice=="1":
            add_expense()
            save_expense()
        elif choice=="2":
            view_expense()
        elif choice=="3":
            search_category()
        elif choice=="4":
            delete_expense()
            save_expense()
        elif choice=="5":
            statistics()
        elif choice=="6":
            filter_expense()
        elif choice=="7":
            sort_expense()
        elif choice=="8":
            break
        else:
            print("Enter known choice")
    else:
        print("The choice must be in digits!")
