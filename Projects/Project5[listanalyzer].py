#List analyzer
numbers=[1,2,3,4,5]
largest=numbers[0]
smallest=numbers[0]
second_largest=float("-inf")
even_count=0
sorting=True
for i in range(len(numbers)):
    if numbers[i] > largest:
        second_largest=largest
        largest=numbers[i]
    elif numbers[i] > second_largest and second_largest!=largest:
        second_largest=numbers[i]
    if numbers[i] < smallest:
        smallest=numbers[i]
    if numbers[i] % 2 ==0:
        even_count+=1
    if i<len(numbers)-1:
        if numbers[i]>numbers[i+1]:
            sorting=False
print("Largest: ",largest)
print("Second largest: ",second_largest)
print("Smallest: ",smallest)
print("Even count: ",even_count)
if sorting:
    print("Sorted")
else:
    print("Not sorted")
    