empty_list = [] 
try:
    while True: 
        numbers = input('Enter ')
        if numbers == 'done':
            break
        empty_list.append(int(numbers))
except: 
    print("That is not a number")
    while True: 
        numbers = input('Enter ')
        if numbers == 'done':
            break
        empty_list.append(int(numbers))
    
first = empty_list[0]
last= empty_list[0]
for empty_list in empty_list:
    if empty_list < first:
        first = empty_list
    elif empty_list > last:
        last = empty_list
print(first, last)


