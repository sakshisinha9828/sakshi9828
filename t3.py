#l = [1,3,4,5,2]
l=eval(input("enter list "))
n = len(l)
count= 0
for i in range(n): 
        if (l[i] % 2): 
            count += 1
total_ele_rem=(min(count, n-count))
print("total_ele_rem",total_ele_rem)
l1=[count+1,n-count]
output=[x for x in l if x not in l1 ]
print("output",output)
