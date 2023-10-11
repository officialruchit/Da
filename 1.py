list = [['B', 'C', 'A'], ['C', 'M', 'A', 'T'], ['B', 'S', 'C'], ['M', 'S', 'C', 'A']]
indiList = []


# Getting Individual List______________________________________________________________________

no_pattern = len(list)
for i in list:
        for j in i:
                if j not in indiList:
                        indiList.append(j)
print(list)
print(indiList)


# 1st Level Starts ___________________________________________________________________________
f = []
ct = 0
for a in indiList:
    for b in list:
        for c in b:
            if (c == a):
                ct = ct + 1
    f.append(ct)
    ct = 0
print(f)

temp = []
temp_itm = []
l = len(indiList)
i = 0
while(i < l):
    if(f[i] >= 2):
        temp_itm.append(indiList[i])
        temp.append(f[i])
    i = i + 1
indiList = temp_itm
f = temp
print(indiList)
print(f)

# Sorting _________[5,7,4,9,3]__________________________________________________________________________
l = len(f)-1 #4
i=0
temp = 0;
for i in range(l):
        while(f[i]<f[i+1]):
                temp = f[i+1]
                f[i+1] = f[i]
                f[i] = temp

                t = indiList[i+1]
                indiList[i+1] = indiList[i]
                indiList[i] = t

print(indiList)
print(f)



# 2nd Level Starts __________________________________________________________________________

l = len(indiList)
newList = []
for i in range(0,len(indiList)):
        for t in range(i+1,l):
                tempList = []
                tempList.append(indiList[i])
                tempList.append(indiList[t])
                newList.append(tempList)
print(newList)
f2 = []
ct = 0
l = len(newList)
i=0
while(i<l):
        temp = newList[i]
        for j in list:
                if(temp[0] in j):
                        if(temp[1] in j):
                                ct = ct+1
        f2.append(ct)
        i = i + 1
        ct = 0
print(f2)

l = len(f2)
i=0
while(i<l):
        if(f2[i] < 2):
                f2.pop(i)
                newList.pop(i)
        i = i + 1
        l = len(f2)
print(newList)
print(f2)






