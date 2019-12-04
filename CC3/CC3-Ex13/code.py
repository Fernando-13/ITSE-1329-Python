def not_string(string):
    x = string[0:3]
    y = string
    if x == 'not':
        return y
    else: 
        z = 'not ' + y
        return z 
print(not_string('not yet'))
        
    