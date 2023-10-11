list = []
temp = []
n = input("Enter Number of Values you want: ")
n= int(n)
for i in range(n):
    t = int(input("Enter the values: "))
    temp.append(t)
    if((i+1)%4==0):
        list.append(temp)
        temp = []
print(list)

newlist = []
temp_1 = []
temp_2 = []
temp_3 = []
for i in list:
    for j in i:
        if(j > 0 and j <= 20):
            temp_1.append(j)
        if(j > 20 and j <= 50):
            temp_2.append(j)
        if(j > 50 and j <= 100):
            temp_3.append(j)
newlist.append(temp_1)
newlist.append(temp_2)
newlist.append(temp_3)
print(newlist)