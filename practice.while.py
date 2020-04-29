x = int (input ('x:'))
count = 0
Jam = 0
while x!= -1:
    Jam = x + Jam 
    count = count + 1
    print (Jam)
    print (count)
    x = int (input('x:'))
    if x == -1 :
        miangin = Jam / count
        print (miangin)
        break
