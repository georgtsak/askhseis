cont=1000000000
import random
while cont>0:
    cont -=1
    y = int(input("Plhktrologhste ton oro akolouthias Fibonacci pou thelete:"))
    def f(y):
        while y<=0:
            y = int(input("LANTHASMENH EISODOS H MHDEN(to opoio paraleipetai)\nPlhktrologhste thetiko oro akolouthias Fibonacci:"))   
        if y==1 or y==2:
           return 1
        else:
           return f(y-1)+f(y-2) #xn = xn−1 + xn−2
        
    p = f(y)

    print "O epilegmenos oros einai o ekshs:",p
    if y==1 or y==2:
        print "O oros pou dothike einai PRWTOS"
    elif y==3:
        print "O oros pou dothike DEN einai prwtos" 
    else:
        sunolo = 0
        for i in range(20):
            a = random.randint(1,p-1)
            if (a**p) % p == a%p: #isxuei an einai prwtos
                sunolo += 1 # sunolo=sunolo+1   
        if sunolo == 20:
            print "O oros pou dothike einai PRWTOS"
        else:
            print "O oros pou dothike DEN einai prwtos"
     
