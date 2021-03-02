#ASKHSH 5 (me SOS)
import random
sumi = 0    #i gia seira
sumj = 0    #j gia sthlh
sumd1 = 0   #d gia diagwnio
sumd2 = 0
x = int(input("Plhktrologhste to platos tou orthogwniou pou thelete:"))
y = int(input("Plhktrologhste to upsos tou orthogwniou pou thelete:"))

while x<3 or y<3:
    print "den tha sxhmatistei kanena SOS. Plhktrologhste kainourgies times"
    x = int(input("Plhktrologhste to platos tou orthogwniou pou thelete:"))
    y = int(input("Plhktrologhste to upsos tou orthogwniou pou thelete:"))
    
pth = x*y  #plithos thesewn
miso = pth/2.0
miso = round(miso) #stroggulopoihsh
miso = int(float(miso)) #metatroph dekadikou se akeraio

 
d = [ ['S' for i in range(x)] for j in range(y) ]  #dhmiourgia multi dimensional listas

div = miso // y
mod = miso % y

for i in range(y):
    for j in range(div):
        d[i][j] = 'O'

if mod >= 1:
    for i in range(mod):
        d[i][mod] = 'O' 

for i in range(100):
    
    random.shuffle(d)
    for sublist in d:
        random.shuffle(sublist)
            

    #grammes
    
    for j in range(y):
        for i in range(x-3):
            if (d[i][j] == 'S' and d[i+2][j] == 'S' and d[i+1][j] == 'O'):
                sumi = sumi + 1

    #sthles
                
    for i in range(x):
        for j in range(y - 3):
            if (d[i][i] == 'S' and d[i][j+2] == 'S' and  d[i][j+1] == 'O') :
                sumj = sumj + 1

    # kuria diagvnios \
    
    for i in range(x - 3):
        for j in range(y - 3):
            if (d[i][j] == 'S' and d[i+2][j+2] == 'S' and d[i+1][j+1] ==  'O'):
                sumd1 = sumd1 + 1
            
    # deuterh diagwnios /
    
    for i in range(x - 3):
        for j in range(3, y):
            if (d[i][j] == 'S' and  d[i+2][j-2] == 'S' and d[i+1][j-1] == 'O'):
                sumd2 = sumd2 + 1


pth1 = pth*1.0
mo1 = sumi/pth1
mo2 = sumj/pth1
mo3 = sumd1/pth1
mo4 = sumd2/x

print "o mesos oros twn SOS pou sxhmatizontai stis grammes einai o ekshs:",mo1
print "o mesos oros twn SOS pou sxhmatizontai stis sthles einai o ekshs:",mo2
print "o mesos oros twn SOS pou sxhmatizontai sthn kuria diagwnio( \ ) einai o ekshs:",mo3
print "o mesos oros twn SOS pou sxhmatizontai sthn deutereuousa diagwnio( / ) einai o ekshs:",mo4



    
