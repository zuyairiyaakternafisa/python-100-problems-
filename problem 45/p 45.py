#Read N and print the sum of all integers from 1 to N using a loop. 
# SAMPLE INPUT SAMPLE OUTPUT 10 55 
n = int (input())
total = 0
for i in range (1,n+1) :
    total = total+i
    print (total) 
