fname = input("Enter file name: ")
fh = open(fname,"r")
words=list()
for line in fh:
    line=line.rstrip()
    wds=line.split()
    
    if len(wds) < 3 or wds[0] != "From":
        continue
    else:
        x=wds[1]
        words.append(x)
counts=dict()
for word in words:
    counts[word]=counts.get(word,0) + 1
#prints emails and how many times they were sent
#print("counts: ",counts)
max_key = max(counts, key=counts.get)
print("The person which sent max e mail: ",max_key)
#mbox-short.txt
