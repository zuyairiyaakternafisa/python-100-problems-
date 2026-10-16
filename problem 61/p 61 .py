#Read a lowercase word and count how many vowels (a, e, i, o, u) it has. 
# SAMPLE INPUT SAMPLE OUTPUT education 5
word = input()
count = 0
for ch in word :
    if ch in "aeiou":
        count = count +1
        print (count)