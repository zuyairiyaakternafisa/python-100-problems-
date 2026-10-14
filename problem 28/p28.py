#Read a number of seconds and convert it into hours, minutes and seconds. 
# SAMPLE INPUT SAMPLE OUTPUT 3725 1 hour(s) 2 minute(s) 5 second
total_seconds = int (input())
hours = total_seconds // 3600
minutes= (total_seconds%3600)//60
second= total_seconds%60

print ("hours (s)",hours,"minutes",minutes,"second",second)