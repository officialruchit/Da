
tran = [["Tea","Milk"],["bread", "butter", "cheese"],["cheese", "chocolate", "cake"],["Milk", "bread", "Tea"],["Tea", "coffee", "butter"]]
iteam = []
for i in tran:
    for j in i:
        if(j not in iteam):
            iteam.append(j)
print(iteam)

ct = 0
te = []

for i in iteam:
    for j in tran:
        for k in j:
            if(k == i):
                ct = ct + 1
    temp = iteam.index(i)
    te.append(ct)

    ct = 0
print(te)


i = 0
c2 = []
while(i < len(iteam)):
    if(te[i] > 1):
        c2.append(iteam[i])
    i = i + 1
print(c2)

i = 0
c3 = []
temp = []
while(i < len(c2)):
    j = i + 1
    while(j < len(c2)):
        #temp = c2[i] + " " + c2[j]
        temp.append(c2[i])
        temp.append(c2[j])
        j = j + 1
        c3.append(temp)
        temp = []
    i = i + 1
print(c3)
ct = 0
l3=[]
for i in c3:
    i1 = i[0]
    i2 = i[1]
    for j in tran:
        if((i1 in j) and (i2 in j)):
            ct = ct+ 1
    l3.append(ct)
    ct = 0
print(l3)

final_c3 = []

i = 0
while(i < len(c3)):
    if(l3[i] > 1):
        final_c3.append(c3[i])
    i = i + 1
print(final_c3)

            
    
