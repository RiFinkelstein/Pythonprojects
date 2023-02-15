#most used charachter in sentance
# can change to userinput
sentance = "the big black dog ran over the moon"
no_space= sentance.strip()
charachter_frequency = {}
for charachter in sentance:
    if charachter in charachter_frequency:
        charachter_frequency[charachter] += 1
    else:
        charachter_frequency[charachter] = 1
sorted = (sorted(charachter_frequency.items(),
          key=lambda kv: kv[1], reverse=True))
print(sorted[0])
