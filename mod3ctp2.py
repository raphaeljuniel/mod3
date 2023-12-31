current_hour = int(input("Enter the current hours, if 12 hour time add 12 to pm times. Example 3pm is 15hrs")) #This will ask the user to input the current number of hours based on a 24hr clock
current_hour = current_hour % 24 # This line will force the integer input to be within a 24hr timeframe 
print(f"your time is: {current_hour}") # This will display the users input back to them
alarm_hours = int(input("Enter future number of hours")) # This line will ask the user to input the future number of hours the alarm is to go off
print(f"The time will be: {(current_hour + alarm_hours) % 24}00hrs") # This line will print out what time it will be when the alarm will go off based on a 24hr timeframe
