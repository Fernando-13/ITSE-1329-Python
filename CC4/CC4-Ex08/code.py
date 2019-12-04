#   open mbox-short.txt, transform to uppercase
fname = input('Enter a file name: ')
file = open(fname)
data = file.read()
print(data.upper())
    