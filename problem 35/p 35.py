#A year is a leap year if it is divisible by 4 and not by 100, unless it is also divisible by 400. Read a year and print Leap Year or Not a Leap Year.
#  SAMPLE INPUT SAMPLE OUTPUT 2024 Leap Year
year = int (input())
if year %400==0:
    print ("Leap Year")
elif year %100 ==0:
    print ("Not a Leap Year")
elif  year %4==0:
    print ("Leap Year")
else:
    print ("Not a Leap Year")