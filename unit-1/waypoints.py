alerts = ["E3", "E8"]

print("Initial alerts:", alerts)

alerts.append("E5")
print("After append:", alerts)

alerts.insert(1, "E1")
print("After insert:", alerts)

alerts.remove("E8")
print("After remove:", alerts)

# List references and copies
first = [5, 10, 15]
second = first
third = first.copy()

second.append(20)
third.append(100)

print("first =", first)
print("second =", second)
print("third =", third)

print("second is first:", second is first)
print("third is first:", third is first)

# Removing invalid readings
sensor_values = [15, -1, 28, -1, 42]

sensor_values = [value for value in sensor_values if value != -1]

print("Clean readings:", sensor_values)

# List comprehensions
readings = [14, 22, 35, 48, 9]

doubled = [value * 2 for value in readings]
large_values = [value for value in readings if value > 25]

print("Doubled:", doubled)
print("Above 25:", large_values)