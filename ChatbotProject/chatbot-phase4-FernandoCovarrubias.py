# Fernando Covarrubias 
count = 1
def random_num():
    import random
    answer = random.randint(1,24)
    return(answer)
def greeter(name, last_name):
    """ Turned the greeter into a function  """
    x = random_num()
    print('The current hours is', x)
    if x in range(1,5):
        return ('Have a good night, ' + name + ' ' + last_name[0])
    elif x in range(5,11):
        return ('Have a good breakfast, ' + name + ' ' + last_name[0])
    elif x in range(11,16):
        return('Have a good lunch, ' + name + ' ' + last_name[0])
    elif x in range(16,21):
        return("Have a good dinner, " + name + ' ' + last_name[0])
    else:
        return('Have a good night, ' + name + ' ' + last_name[0])
# used function inside loop
while True:
    name = input('What is your first name? ')
    last_name = input('Whats is your last name? ')
    print(greeter(name, last_name))
    greeting = input('Would you like another greeeting? ')
    if greeting == "no":
        break
    count = count + 1 
        
print('You received', count, 'greetings')