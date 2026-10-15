#Read marks (0-100). Grades: 80 or more = A, 60 to 79 = B, 40 to 59 = C, below 40 = Fail. Print the grade. 
# SAMPLE INPUT SAMPLE OUTPUT 85 Grade: A
marks = int (input())
if marks >= 80:
    print ("A")
elif marks >= 60:
    print ("B")
elif marks >=  40:
    print ("C")
else :
    print ("Fail")