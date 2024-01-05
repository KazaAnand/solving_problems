

l1=list(map(int,input('l1 nos').split()))
l2=list(map(int,input('l2 nos').split()))
l3=[]
l1.sort()
l2.sort()
print(l1)
print(l2)
for i in range(len(l1)):
    if l1[i]<l2[i]:
        l3.append(l1[i])
        l3.append(l2[i])
    elif l1[i]>l2[i]:
        l3.append(l2[i])
        l3.append(l1[i])
    else:
        l3.append(l1[i])
        l3.append(l2[i])
print(l3)




