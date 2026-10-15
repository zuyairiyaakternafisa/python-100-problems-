#Read three integers on one line separated by spaces and print the largest one. 
# SAMPLE INPUT SAMPLE OUTPUT 12 45 30 45
a,b,c= map (int,input().split())
if a>b and a>c:
    print (a)
elif b>a and b>c:
    print (b)
else:
    print(c)