import random
Javab = random.randint(1 , 99)
hads = int(input ('what is your NUM ?'))

while hads != Javab :
    if hads > Javab:
        print ('mine is smaller')
    else:
        print ('mine is lorger')
    hads = int (input('what is your NUM? '))
print ('You WON')
