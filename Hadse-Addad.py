a = 1
b = 99
import random   
hads = random.randint (a , b)
print (hads)
Javab = input ('User idea:')
while Javab != 'WON':
    if Javab == 'larger':
        a = hads + 1
        hads = random.randint (a , b)
        print (hads)
        Javab = input ('User idea:')
    elif Javab == 'smaller':
        b = hads - 1
        hads = random.randint (a , b)
        print (hads)
        Javab = input ('User idea:')
    else :
        Javab = input ('please choise on of them : WON , smaller , larger ')
print ('EYVAL')