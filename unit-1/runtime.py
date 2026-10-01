battery = int(input("Enter current battery percentage: "))
print("Battery after boost:", battery + 10)

robot = "RoverX"
charge = 82.75

print("Robot", robot, "has", charge, "% battery")
print(f"Robot {robot} has {charge}% battery")
print(f"Robot {robot} has {charge:.1f}% battery")
print(f"{robot:<10} | {charge:>6.2f}%")

print("--------------------")

capacity = float(input("Enter battery capacity (mAh): "))
current = float(input("Enter current consumption (mA): "))

if current > 0:
    runtime = capacity / current
    print(f"Estimated runtime: {runtime:.2f} hours")
else:
    print("Current consumption must be greater than zero.")