try:
    hours = input('Enter Hours ')#your code goes here
    rate = input('Enter Rate ')#your code goes here
    if float(hours) > 40 :
        ot = (float(hours) - 40) * (float(rate) * 1.5)
        print('Pay:' , 40 * float(rate) + ot)
    else: 
        print('Pay:' , float(hours) * float(rate)) # Add your code below
except: 
    print('Error, please enter a numeric input')

#try:
#    hours = input('Enter Hours: ')#your code goes here
#    hours = float(hours)
#    rate = input('Enter Rate: ')#your code goes here
#    rate = float(rate)
#    if hours > 40 :
#        ot = (hours - 40) * (rate * 1.5)
#        print('Pay:' , 40 * rate + ot)
#   else: 
#        print('Pay:' , hours * rate) # Add your code below
#except:
#    print('Error, please enter a numeric input')

    

