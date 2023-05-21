input=[1,0,1,0,1,0,0,1]
zero=[]
one=[]
for i in input:
    if i==0:
        zero.append(i)
    elif i==1:
        one.append(i)
sorted_list=zero+one
print (sorted_list)
