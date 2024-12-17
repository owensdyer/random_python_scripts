# Declare variables
MINS_IN_HOUR = 60


# Input
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))


# Get the duration of time in hours and minutes
dura_hour = dura // MINS_IN_HOUR
dura_mins = dura % MINS_IN_HOUR


# Adding hours and mins to current time
if not dura_hour:
    mins += dura_mins
else:
    hour += dura_hour
    mins += dura_mins


# Checking time in correct format
# Increment the hour if mins over 60
if mins >= 60:
    hour += 1
    mins -= 60


if hour >= 24:
    hour %= 24
    next_day = True
else:
    next_day = False


# Display the time
print("The ending will be at:", str(hour) + ":" + str(mins), end="")

if next_day:
    print(" - +1 day")
else:
    print()
