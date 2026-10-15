#Three sides form a valid triangle if the sum of any two sides is greater than the third side. Read three sides on one line and print Valid Triangle or Invalid Triangle. 
# SAMPLE INPUT SAMPLE OUTPUT 3 4 5 Valid Triangle
a,b,c = map (int, input().split())
if (a+b>c) and (a+c>b) and (b+c>a):
    print ("Valid Triangle")
else :
    print ("Invalid Triangle")