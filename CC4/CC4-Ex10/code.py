fname = input('Enter a file name: ')
fopen = open(fname)
count = 0 
total = 0
avr = 0 
for file in fopen:
    if file.startswith('X-DSPAM-Confidence'):
        x = float(file[19:])
        count += 1
        total = x + total 
        avr = total /count
print('Average spam confidence:' , avr)
