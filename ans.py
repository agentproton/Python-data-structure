import re
filename=input("enter file name")
fhand=open(filename)
sum=0
for line in fhand:
    line=line.strip()
    if(re.search('[0-9]+',line)):
        str=re.findall('[0-9]+',line)
        for s in str:
            sum+=int(s)
print(sum)
