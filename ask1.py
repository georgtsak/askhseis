#ASKHSH 1
import random
x = int(input("Plhktrologhste tis diastaseis tou tetragwnou pou thelete:"))
while x < 4:
    x = int(input("den tha sxhmatistei kamia 4ada! Plhktrologhste arithmo megalutero h iso tou 4:"))
sumi = 0
sumj = 0
sumd1 = 0
sumd2 = 0

pth = x**2  #plithos thesewn
miso = pth/2.0
miso = round(miso) #stroggulopoihsh
miso = int(float(miso)) #metatroph dekadikou se akeraio
    
d = [ [0 for i in range(x)] for j in range(x) ]  #dhmiourgia multi dimensional listas

div = miso // x
mod = miso % x

for i in range(x):
    for j in range(div):
            d[i][j] = 1

if mod >= 1:
    for i in range(mod):
        d[i][mod] = 1  


for i in range(100):
    
    random.shuffle(d)
    for sublist in d:
        random.shuffle(sublist)
    

    #grammes
    
    for j in range(x):
        for i in range(x-3):
            if d[i][j] == d[i+1][j] == d[i+2][j] ==  d[i+3][j] == 1:
                sumi = sumi + 1

    #sthles
                
    for i in range(x):
        for j in range(x - 3):
            if d[i][i] == d[i][j+1] == d[i][j+2] == d[i][j+3] == 1:
                sumj = sumj + 1


    # kuria diagvnios \
    
    for i in range(x - 3):
        for j in range(x - 3):
            if d[i][j] ==  d[i+1][j+1] == d[i+2][j+2] == d[i+3][j+3] == 1:
                sumd1 = sumd1 + 1
            
    # deuterh diagwnios /
    
    for i in range(x - 3):
        for j in range(3, x):
            if d[i][j] ==  d[i+1][j-1] ==  d[i+2][j-2] ==  d[i+3][j-3] == 1:
                sumd2 = sumd2 + 1


pth1 = pth*1.0
mo1 = sumi/pth1
mo2 = sumj/pth1
mo3 = sumd1/pth1
mo4 = sumd2/pth1

print "o mesos oros twn tetradwn stis grammes einai o ekshs:",mo1
print "o mesos oros twn tetradwn stis sthles einai o ekshs:",mo2
print "o mesos oros twn tetradwn sthn kuria diagwnio( \ ) einai o ekshs:",mo3

print "o mesos oros twn tetradwn sthn deutereuousa diagwnio( / ) einai o ekshs:",mo4


    
