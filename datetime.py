import datetime

# Get the current system time
x = datetime.datetime.now()

# Format the time
print(x.year)
print(x.strftime("%A"))
print(x.strftime("%B"))
print(x.strftime("%d-%m-%Y, %H:%M:%S%p"))
print(x.strftime("%c"))

# Creating Date Object
x = datetime.datetime(2020, 5, 17)
print(x)