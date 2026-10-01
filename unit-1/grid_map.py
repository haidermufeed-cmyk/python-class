waypoints = [(1, 1), (3, 2), (6, 4)]

for point in waypoints:
    print("Moving toward:", point)

print("--- Scan Cycle ---")

for count in range(1, 4):
    print("Scan", count)

print("--- Numbers ---")

for number in range(2, 7):
    print(number, end=" ")

print()

for number in range(12, 0, -3):
    print(number, end=" ")

print()

# Accumulator pattern
sensor_data = [21.4, 22.8, 20.9, 23.5, 22.1]
total = 0

for value in sensor_data:
    total += value

print(f"Total: {total:.2f}")
print("Readings:", len(sensor_data))
print(f"Average: {total / len(sensor_data):.2f}")

# Nested loops
blocked = [(1, 3), (2, 2), (4, 1)]

print("--- Grid ---")

for row in range(5):
    for column in range(5):
        if (row, column) in blocked:
            print("#", end=" ")
        else:
            print(".", end=" ")
    print()

# 8x8 robot grid
obstacles = [(2, 4), (4, 6), (6, 2), (3, 1)]

print("--- Robot Map ---")

for row in range(8):
    for column in range(8):
        position = (row, column)

        if position in obstacles:
            print("X", end=" ")
        elif position == (0, 0):
            print("S", end=" ")
        elif position == (7, 7):
            print("G", end=" ")
        else:
            print(".", end=" ")

    print()

# Continue and break
readings = [18, -2, 42, 75, 31]

for value in readings:
    if value < 0:
        continue

    if value > 70:
        print("Danger detected:", value)
        break

    print("Reading safe:", value)