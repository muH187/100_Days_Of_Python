import time

timestamp = time.strftime("%H:%M:%S")
print("Your Current Time is", timestamp)

hour = int(time.strftime("%H"))

if hour >= 4 and hour <= 12:
    print("Good Morning Sir")
elif hour >= 13 and hour <= 16:
    print("Good Evening Sir")
elif hour >= 17 and hour <= 20:
    print("Good Evening Sir")
else:
    print("Good Night Sir")