#Currency Converter
amount=float(input("Enter the amount: "))
while True:
    source=input("Source Currrency (USD/EUR/CAD): ").upper()
    target=input("Target Currency (USD/EUR/CAD): ").upper()
    if source=="USD":
        if target=="EUR":
            result=amount*0.88
            print(f'{amount} USD is equal to {result:.2f} EUR')
        elif target=="CAD":
            result=amount*1.42
            print(f'{amount} USD is equal to {result:.2f} CAD')
        break
    elif source=="EUR":
        if target=="USD":
            result=amount*1.14
            print(f'{amount} EUR is equal to {result:.2f} USD')
        elif target=="CAD":
            result=amount*1.62
            print(f'{amount} EUR is equal to {result:.2f} CAD')
        break
    elif source=="CAD":
        if target=="USD":
            result=amount*0.70
            print(f'{amount} CAD is equal to {result:.2f} USD')
        elif target=="EUR":
            result=amount*0.62
            print(f'{amount} CAD is equal to {result:.2f} EUR')
        break
    else:
        print("Invalid source currency!")
        