from Myro import*
from random import*

movieList1=["walk","ball","call","dead","river","face","shoe","car","jump","phone"]
movieList2=["bag","paper","water","return","jurassic","killer","robots","dragons","terminator","juice"]
movieList3=["puppets","dogs","charger","sword","jaws","knight","night","avenger","magic","money"]
movieList4=["of","the","for","with","are", "it","when","by","in","a"] 

i=0
while i<10:
    num=randrange(10)
    element1=movieList1[num]
    num=randrange(10)
    element2=movieList2[num]
    num=randrange(10)
    element3=movieList3[num]
    num=randrange(10)
    element4=movieList4[num]
    print(element2,element1,element4,element3)
    i=i+1
