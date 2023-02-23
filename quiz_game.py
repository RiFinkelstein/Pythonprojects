print("welcome to my quiz!")

playing= input("do you want to play? ")
score=0
if playing != "yes":
    quit()

print("okay! lets play:)")

answer = input("what is my full name? ").lower
if answer== "rivka finkelstein":
    print('correct!')
    score+=1
else:
    print("incorrect")
