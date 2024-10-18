#input
time = float(input("Enter a time duration in hours: "))

#convert the time duration to minutes and seconds

minutes = float(time * 60)
seconds = float( time * 3600)

#processing
time_duration = minutes, seconds

#output
#print("The time duration in minutes is: ", minutes, "and in seconds: ", seconds)
print("Time duration converted to minutes and seconds: ", time_duration)