# Write a function to make an hour-to-minute converter.

def hour_to_minutes(hours):
    """Convert hours to minutes."""
    return hours * 60


# take input from the user
hours = float(input("Enter the number of hours: "))

# if a user enters a negative number
if hours <= 0:
    print("Please enter a positive number: ")
    hours = float(input("Enter the number of hours: "))
    

# convert hours to minutes
minutes = hour_to_minutes(hours)

# showing the result in minutes
print(f"{hours} hours is equal to {minutes} minutes.")
