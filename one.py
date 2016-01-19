#!/usr/bin/python

print('Calculating...')
myList=[]
x=0

for i in range(1, 1000):
        if(i%3)==0 or (i%5)==0:
                print('Appended...')
                myList.append(i)

myList = map(int, myList)
x = sum(myList)
print(x)
