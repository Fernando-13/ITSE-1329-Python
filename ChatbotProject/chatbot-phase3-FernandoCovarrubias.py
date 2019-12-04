#Fernando Covarrubias 
count = 1
def greeter(name, last_name, time):
    """ Turned the greeter into a function  """
    if time == 'Morning':
        return ('Have a good breakfast, ' + name + ' ' + last_name[0])
    elif time == 'Afternoon':
        return ('Have a good lunch, ' + name + ' ' + last_name[0])
    elif time == 'Evening':
        return('Have a good dinner, ' + name + ' ' + last_name[0])
    else:
        return("Have a good one, " + name + ' ' + last_name[0])
# used function inside loop
while True:
    name = input('What is your first name? ')
    last_name = input('Whats is your last name? ')
    time = input('What time of day is it (Morning, Afternoon, Evening): ' )
    print(greeter(name, last_name, time))
    greeting = input('Would you like another greeeting? ')
    if greeting == "no":
        break
    count = count + 1 
        
print('You received', count, 'greetings')

