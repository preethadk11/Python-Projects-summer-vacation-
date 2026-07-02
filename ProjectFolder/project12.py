import requests
API_KEY="36b17f40af66cb540d17c23c56fb3902"
url=f'http://api.exchangeratesapi.io/v1/latest?access_key={API_KEY}'
response=requests.get(url)
data=response.json()
rates=data["rates"]
count=0
history=[]
available_currencies=[]
print("Available currencies\n------------")
for cur in rates.keys():
    available_currencies.append(cur)
    print(cur,end=" ")
    count+=1
    if count==5:
        print()
        count=0
def conversion(base,amount):
    while True:
        target=input("Enter the target currency: ").upper()
        if target in rates:
            base_rate=data["rates"][base]
            target_rate=data["rates"][target]
            convert=amount*(target_rate/base_rate)
            return convert, target
        else:
            print("Invalid target currency!")

def multipleconversion(base,amount):
    currency=[]
    conversion=[]
    many=int(input("How many currency do you want to convert to: "))
    for i in range(many):
        cur=input(f'Enter currency {i+1}: ')
        currency.append(cur.upper())
    for curr in currency:
        base_rate=rates[base]
        target_rate=data["rates"][curr]
        convert=amount*(target_rate/base_rate)
        conversion.append(f'{amount} {base} to {convert:.2f} {curr}')
    return conversion

    
menu="\t\tCurrency Convertor\n\n1.Converting to one currency\n2.Converting to multiple currencies\n"
while True:
    print(menu)
    choice=input("Enter the choice: ")
    if choice.isdigit():
        if choice=="1":
            amount=float(input("Enter the amount: "))
            while True:
                base=input("Enter the base currency: ").upper()
                if base in rates.keys():
                    result,target=conversion(base,amount)
                    print(f'{result:.2f} {target}')
                    history.append(f'{amount} {base} to {result:.2f} {target}')
                    break
                else:
                    print("Invalid base currency!")
        elif choice=="2":
            amount=float(input("Enter the amount: "))
            while True:
                base=input("Enter the base currency: ").upper()
                if base in rates.keys():
                    result=multipleconversion(base,amount)
                    for cur in result:
                        print(cur)
                        history.append(cur)
                    break
                else:
                    print("Invalide base currency!")            
    else:
        print("Invalid choice")
    again=input("CONTINUE? (yes/no): ").lower()
    if again != "yes":
        break
print("History------------")
for i in range(len(history)):
    print(history[i])

    
   


