nums=[8, 7, 2, 5, 3, 1]
target =10 
foundPair=False
for i in range(len(nums)-1):
    for j in range(i +1, len(nums)):
        if nums[i]+nums[j]==target:
            foundPair= True
            print('found a pair', nums[i], nums[j])

if not foundPair:
    print('no pairs found')
