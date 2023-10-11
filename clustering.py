l =[]
ans =[]
n = int(input("Enter your value"))
 

for i  in range(n):
    v = int(input("Enter number"))
    l.append(v)
print(l)
i =0
ln = len(l)
cl = int(input("Enter the number of cluster"))
for j in range(cl):
    temp = []
    ans.append(temp)
print(ans)
 

st = 0
for j in ans:
    d = st
    while(d < ln):
        j.append(l[d])
        d = d + cl
    st =st + 1
    print(j)
print(ans)
print(cl)
count = 0


for a in range(cl):
    print("cluster",a)
