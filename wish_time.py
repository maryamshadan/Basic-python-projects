
from time import strftime

hour = int(strftime("%H"))  # Extract hour (00-23) as an integer
ampm = strftime("%p")       # Extract AM/PM

tm=(strftime("%H:%M:%S %p"))
print(tm)

if (hour>=00 and hour<12) and ampm=="AM":
    print("good morning")

elif (hour>=12 and hour<17) and ampm=="PM":
    print("good afternoon")

elif (hour>=17 and hour<20)and ampm=="PM" :
    print("good evening")

else :
    print("good night")