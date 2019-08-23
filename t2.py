s=input("enter string")
l=[]
for value in s:
    if value not in l:
        l.append(value)
        l.append(s.count(value))
        l1=[int(x) for x in l[1::2]]
        t=l.index(max(l1))
print(l[t-1])