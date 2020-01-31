tot=int(input("enter number of students"))
n=1
i=1
list=[]
while i<=tot:
    w=int(input('enter weight %d' %n))
    n=n+1
    list.insert(i,w)
    i=i+1
print("weight in lb:",list)
list2=[w*0.45 for w in list if range(0,tot)]
print("weights in kg:",list2)