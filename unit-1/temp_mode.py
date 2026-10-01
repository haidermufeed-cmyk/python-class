temperature = 42.5

if temperature > 40:
    print("Cooling system activated")

print("Temperature check finished")

# Temperature-based operating mode
temperature = float(input("Enter enclosure temperature: "))

if temperature < 35:
    mode = "Heating"
elif temperature <= 40:
    mode = "Normal"
elif temperature <= 55:
    mode = "Cooling"
else:
    mode = "Emergency shutdown"

print("Operating mode:", mode)

# Grade check
marks = 87

if marks >= 90:
    grade = "DISTINCTION"
elif marks >= 40:
    grade = "PASS"
else:
    grade = "FAIL"

print("Result:", grade)