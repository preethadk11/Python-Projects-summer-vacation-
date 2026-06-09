numbers=[5,4,3,2,1]
largest=numbers[0]
smallest=numbers[0]
second_largest=float("-inf")
even_count=0
is_asc=True
is_des=True
for i in range(len(numbers)):
    if numbers[i]>largest:
        second_largest=largest
        largest=numbers[i]
    elif numbers[i]>second_largest and numbers[i]!=largest:
        second_largest=numbers[i]
    if numbers[i]<smallest:
        smallest=numbers[i]
    if numbers[i]%2==0:
        even_count+=1
    if i<len(numbers)-1:
        if numbers[i]>numbers[i+1]:
            is_asc=False
        if numbers[i]<numbers[i+1]:
            is_des=False
print(f'Largest: {largest}')
print(f'Smallest: {smallest}')
print(f'Second_largest: {second_largest}')
print(f'Even count: {even_count}')
if is_asc:
    print("Sorted in ascending order")
else:
    print("Sorted in descending order")