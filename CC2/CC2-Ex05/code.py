hours = input('Enter Hours ')#your code goes here
rate = input('Enter Rate ')#your code goes here
if float(hours) > 40 :
    ot = (float(hours) - 40) * (float(rate) * 1.5)
    print('Pay:' , 40 * float(rate) + ot)
else: 
    print('pay: ' , float(hours) * float(rate)) # Add your code below

