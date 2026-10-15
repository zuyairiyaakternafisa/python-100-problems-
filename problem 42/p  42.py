#Read a number from 1 to 7 (1 = Monday) and print the day name. For any other number print Invalid number. 
# SAMPLE INPUT SAMPLE OUTPUT 3 Wednesday
day = int (input ())
if day == 1:
    print ("Monday")
elif day ==2:
    print ("Tuesday")
elif day ==3:
    print ("Wednesday")
elif day ==4:
    print ("Thursday")
elif day ==5:
    print ("Friday")
elif day ==6:
    print ("Saturday")
elif day ==7:
    print("Sunday")
else:
    print ("Invalid number")