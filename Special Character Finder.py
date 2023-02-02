import operator
import sys

import operator
import sys

if len(sys.argv) < 3:
    print("error")
    sys.exit()

fname = sys.argv[1]
ReadStory = open(fname, "r")
filecontent = ReadStory.read()
lowcasecontent = filecontent.casefold()
ReadStory.close()

filename1 = sys.argv[2]
readstoryskip = open(filename1, "r")
fileskip = readstoryskip.read()
readstoryskip.close()

erasures = ['\n','\t','.','?','!',',',';',':','\'','\"']
for i in erasures:
    lowcasecontent = lowcasecontent.replace(i, " ")

fileskip = fileskip.replace(',', " ")

read_string = lowcasecontent.split()
skip_string = fileskip.split()

for i in range(len(skip_string)):
    for j in range(len(read_string)):
        if skip_string[i] == read_string[j]:
            read_string[j] = " "

fixedlist = []
for i in read_string:
    if i != " ":
        fixedlist.append(i)


diction = {}

for ii in range(len(fixedlist) - 1):
    jj = ii + 1
    tmp = fixedlist[ii] + " " + fixedlist[jj]
    if tmp not in diction:
        diction[tmp] = 0
    if tmp in diction:
        diction[tmp] = diction[tmp]+1


datakeys = diction.keys()

print("the five most occuring words are ")
prnt = sorted(diction.items(), key=operator.itemgetter(1), reverse = True)
for ii in range(5):
    print(prnt[ii])
    
    

