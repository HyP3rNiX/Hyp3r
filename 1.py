import re
f = open(input("Enter path"),"r")
s = f.read()
#s = str(input("Enter string: ")).lower().split()
ss = re.sub("[^a-zA-Z]"," ", str(s)).lower().split(" ")

count={}
for i in ss:
    if i in count:
        count[i] +=1
    else:
        count[i] = 1

print(count)