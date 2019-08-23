d={2:["a","b","c"],3:["d","e","f"],4:["g","h","i"],5:["j","k","l"],6:["m","n","o"],7:["p","q","r","s"],8:["t","u","v"],9:["w","x","y","z"]}
key=input("enter key")
i=0
count=1
result=''
while(i<len(key)):
    if(i<len(key)-1 and key[i]==key[i+1]):
        count+=1
    else:
        result+=d[int(key[i])][count-1]
        count=1
    i+=1
print(result)
