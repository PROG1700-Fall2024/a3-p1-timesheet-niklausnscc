#Program 1 – Timesheet
#Description:   Design and write a program that accepts the number of hours worked on 
#               each of five work days from the user, then displays different 
#               information calculated about those entries as output. 

#Student #: W0414211   
#Student Name: Niklaus Guenther

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
#Get hours worked for each day
    hours = []
    for i in range(5):
        while True:
            try:
                h = float(input(f"Enter hours worked for Day {i + 1}: "))
                if h < 0:
                    print("Hours cannot be negative. Try again.")
                    continue
                hours.append(h)
                break
            except ValueError:
                print("Invalid input. Enter a number.")
    #Find the maximum hours and the days with those hours
    maxHours = max(hours)
    maxDays = []
    for i in range(len(hours)):
        if hours[i] == maxHours:
            maxDays.append(i + 1)
    #Calculate total and average hours
    totalHours = sum(hours)
    averageHours = totalHours / len(hours)

    #Find days with less than 7 hours worked
    lowDays = []
    for i in range(len(hours)):
        if hours[i] < 7:
            lowDays.append(i + 1)

    print("Time Sheet Summary")
    print(f"Hours worked each day: {hours}")
    print(f"Most hours worked ({maxHours}) on day(s): {maxDays}")
    print(f"Total hours worked: {totalHours}")
    print(f"Average hours per day: {averageHours:.2f}")
    if lowDays:
        print(f"Days with less than 7 hours: {lowDays}")
    else:
        print("No days with less than 7 hours.")
    # YOUR CODE ENDS HERE

main()