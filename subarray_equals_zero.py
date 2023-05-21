Input= [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
n=len(Input)
zero= False

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if Input[i]+Input[j]+Input[k]==0:
                zero=True
                print('these numbers add up to 0', Input[i], Input[j], Input[k])
if not zero:
    print ('there is not combination of numbers to add up to 0')
