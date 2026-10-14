def calculateCalories(weight, activity, minutes):
    if activity == "running":
        caloriesPerMin = weight / 10.5
    else:
        caloriesPerMin = weight / 15.5
    numCalories = caloriesPerMin * minutes
    
    return numCalories

# Main
print("Enter your name: ")
name = input()
print("Enter the number of sessions: ")
numSessions = int(input())
totalCalories = 0
for i in range(1, numSessions + 1, 1):
    print("Enter your weight in kilograms")
    weight = float(input())
    print("Enter the activity (running or walking: ")
    activity = input()
    print("Enter the duration in minutes: ")
    minutes = int(input())
    sessionCalories = calculateCalories(weight, activity, minutes)
    sessionCalories = calculateCalories(weight, activity, minutes)
    totalCalories = totalCalories + sessionCalories
    print("Calories burned for session " + str(i) + ": " + str(sessionCalories))
print("Name: " + name)
print("Total calories burned: " + str(totalCalories))
