l=eval(input("enter list of restaurant"))
for value in l:
        if(value[1]=='Italian' and value.count(5)>0 and 1 not in value):
            print(value[0])
            
