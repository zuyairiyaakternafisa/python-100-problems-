#Read a person's age. If the age is 18 or more print Eligible to vote, otherwise print Not eligible to vote. 
# SAMPLE INPUT SAMPLE OUTPUT 17 Not eligible to vote
age = int (input())
if age>=18:
    print ("Eligible")
else:
    print ("Not eligible")