LIMIT = 65.0
sensor_readings = []

while True:
    print("\n1. Add reading   2. Show report   3. Exit")
    option = input("Enter choice: ")

    if option == "1":
        reading = float(input("Enter sensor value: "))
        sensor_readings.append(reading)
        print("Reading added.")

    elif option == "2":
        if len(sensor_readings) == 0:
            print("No sensor readings available.")
            continue

        warning_count = 0

        for reading in sensor_readings:
            if reading > LIMIT:
                warning_count += 1

        average = sum(sensor_readings) / len(sensor_readings)

        print("Total readings:", len(sensor_readings))
        print(f"Average value: {average:.2f}")
        print("Warnings:", warning_count)

    elif option == "3":
        print("Mission console stopped.")
        break

    else:
        print("Invalid choice. Try again.")