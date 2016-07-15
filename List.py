myList1=[10,11,12,13,14,15,16,17,18,19,20]

myList2=[0,0,0,0,0]
print(len(myList2))

myList3=[]

i=0
while i<5:
        myList2[i]=0
        i+=1

myList5=["a",5,"doodle",3,10]
print(len(myList5))

myList6=["a",5,"doodle",3,10]
del myList6[3]
print (myList6)

myList7=["a",5,"doodle",3,10]
myList7.append(1738)
print (myList7)

myList8=["a",5,"doodle",3,10]
myList8[0]=8.4
print (myList8)

myList9=["a",5,"doodle",3,10]
myList9.insert(0,300)
print (myList9)

myList10=[]
i=1
while i<10:
    myList10.append(i)
    i=i+2
print (myList10)

