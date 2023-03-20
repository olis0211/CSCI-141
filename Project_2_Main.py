from Project_2 import *
import random
#part I
x = 0
numberlist = []
while x < 50:
    new = make_phone_number()
    numberlist += [new]
    x += 1
print(numberlist)


#part II
x=0
numberlist=[]
for x in range(50):
    new = make_phone_number(sep = '*')
    numberlist += [new]
    x+= 1
print(numberlist)

#part III
x=0
number_list=[]
while x<50:
    new=make_phone_number(['937'],[','])
    numberlist += [new]
print(numberlist)

#part IV
numberlist=[]
for number in range(100):
    new = make_phone_number(['503'])
    numberlist+=[new]
print(numberlist)

