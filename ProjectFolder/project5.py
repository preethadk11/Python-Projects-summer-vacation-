#List analyzer finding all requirements in one traversal
numbers=[90,90,89]
largest=numbers[0]
smallest=numbers[0]
second_largest=float("-inf")
even_count=0
odd_count=0
sum_num=0
avg=0
is_asc=True
is_des=True
for i in range(len(numbers)):
    if numbers[i]>largest:
        second_largest=largest
        largest=numbers[i]
    elif numbers[i]>second_largest and numbers[i]<largest:
        second_largest=numbers[i]
    if numbers[i]<smallest:
        smallest=numbers[i]
    if numbers[i]%2==0:
        even_count+=1
    else:
        odd_count+=1
    if i<len(numbers)-1:
        if numbers[i]>numbers[i+1]:
            is_asc=False
        elif numbers[i]<numbers[i+1]:
            is_des=False
    sum_num+=numbers[i]
print(f'Largest: {largest}')
print(f'Second largest: {second_largest}')
print(f'Smallest: {smallest}')
print(f'Even count: {even_count}\nOdd count: {odd_count}')
if is_asc:
    print("Sorted in ascending order")
elif is_des:
    print("Sorted in descending order")
else:
    print("Not sorted")
print(f'Sum of all numbers: {sum_num}')
print(f'Average: {sum_num/len(numbers):.2f}')