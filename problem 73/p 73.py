#Read integers on one line and print the list elements in reverse order, separated by spaces. SAMPLE INPUT SAMPLE OUTPUT 1 2 3 4 5 5 4 3 2 1
numbers= input().split()
numbers.reverse()
print (*numbers)