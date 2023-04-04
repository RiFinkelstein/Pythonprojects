#this code genrates 100 rqandom numbers between 1 and 10 and then counts the frequency of each number 
import random

# generate 100 random numbers between 1 and 10
numbers = [random.randint(1, 10) for i in range(100)]

# count the frequency of each number
frequency = {}
for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1

# print the frequency of each number
for number, count in frequency.items():
    print(f"{number}: {count}")
