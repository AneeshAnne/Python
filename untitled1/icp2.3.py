inputfile=open(r"C:\Users\anees\OneDrive\Desktop\New folder\sample.txt",'r')
d=dict()
for line in inputfile:
    words=line.strip().split(" ")
    for word in words:
        if word in d:
            d[word]= d[word]+1
        else:
             d[word]=1
for key in list(d.keys()):
     print(key,d[key])