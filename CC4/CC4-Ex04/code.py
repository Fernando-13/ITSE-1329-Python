#import os
#print(os.getcwd())
with open ('mbox-short.txt', 'r') as file:
    count = 0
    for line in file:
        count += 1  # this same as count = count + 1
print(count)

#/home/ec2-user/environment/ITSE-1329-Python/CC4/CC4-Ex04/mbox-short.txt