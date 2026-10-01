robot = {
    "name": "RoverX",
    "battery": 86,
    "mode": "manual"
}

print("Robot:", robot)
print("Name:", robot["name"])

robot["battery"] -= 8
robot["speed"] = 0.6

print("Updated:", robot)
print("Keys:", list(robot.keys()))
print("Values:", list(robot.values()))

# Accessing a missing key safely
robot = {
    "name": "RoverX",
    "battery": 86
}

print("Speed:", robot.get("speed"))
print("Default speed:", robot.get("speed", 0.0))
print("Has speed?", "speed" in robot)

# Count error frequency
events = ["E3", "E5", "E3", "E1", "E5", "E3"]

frequency = {}

for event in events:
    frequency[event] = frequency.get(event, 0) + 1

print("Frequency:", frequency)

for event in sorted(frequency):
    print(f"{event} occurred {frequency[event]} time(s)")

# Character frequency
name = "rover"

letter_count = {}

for letter in name:
    letter_count[letter] = letter_count.get(letter, 0) + 1

print("Letter counts:", letter_count)

for letter in sorted(letter_count, key=letter_count.get, reverse=True):
    print(f"{letter} occurred {letter_count[letter]} time(s)")

most_common = max(letter_count, key=letter_count.get)
print("Most frequent letter:", most_common)