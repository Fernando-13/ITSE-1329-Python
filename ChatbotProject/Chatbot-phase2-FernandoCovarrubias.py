# Fernando Covarrubias 
count = 1
while True:
    name = input('What is your first name? ')
    last_name = input('Whats is your last name? ')
    time = input('What time of day is it (Morning, Afternoon, Evening):' )
    if time == 'Morning':
        print('Have a good breakfast,', name, last_name[0])
    elif time == 'Afternoon':
        print('Have a good lunch,', name, last_name[0])
    elif time == 'Evening':
        print('Have a good dinner,', name, last_name[0])
    else:
        print("Have a good one,", name, last_name[0])
    greeting = input('Would you like another greeeting?')
    if greeting == "no":
        break
    count = count + 1 
        
print('You received', count, 'greetings')
# Made a loop and just added a break condition to stop the loop.
        
