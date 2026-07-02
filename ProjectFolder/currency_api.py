import requests
API_KEY="9ac1dc3f4ae07d875abde85a7a24b3bc"
url=f'http://api.exchangeratesapi.io/v1/latest?access_key={API_KEY}'
response=requests.get(url)
data=response.json()
rates=data["rates"]
count=0
history=[]
print("Available currencies\n--------------------------------------")
for cur in rates.keys():
    print(cur,end=" ")
    count+=1
    if count==10:
        print()
        count=0
def conversion(base,target):
    base_rate=data["rates"][base]
    target_rate=data["rates"][target]
    converted=amount*(target_rate/base_rate)
    return converted
while True:
    print()
    amount=float(input("Enter the amount: "))
    base=input("Enter the base currency: ").upper()
    target=input("Enter the target currency: ").upper()
    result=conversion(base,target)
    print(f'{result:.2f} {target}')
    history.append(f'{amount} {base} To {result:.2f} {target}')
    again=input("Continue? (yes/no): ").lower()
    if again!="yes":
        break
print("History\n------------------")
for i in range(len(history)):
    print(history[i])
    
   


