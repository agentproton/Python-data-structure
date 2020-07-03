#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
#After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lst=dict()
for line in handle:
    line=line.rstrip()
    if line.startswith('From '):
        word=line.split()
        lst[word[1]]=lst.get(word[1],0)+1
                
                
mxcount=0
for a,b in lst.items():
    if mxcount==0 or b>mxcount:
        mxcount=b
        mxword=a
        
print(mxword,mxcount)
