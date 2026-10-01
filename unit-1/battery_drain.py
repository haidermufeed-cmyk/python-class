battery = 95
elapsed = 0

while battery > 25:
    battery -= 8
    elapsed += 1

print(f"Battery warning after {elapsed} minutes: {battery}%")

# Show battery level after every drain
battery = 90
minute = 0

while battery > 30:
    minute += 1
    battery -= 6
    print(f"Minute {minute:02d} -> {battery}%")

print("Battery threshold reached")

# Validate battery input
while True:
    reading = float(input("Enter battery level (0-100): "))

    if 0 <= reading <= 100:
        break

    print("Invalid value. Enter a number between 0 and 100.")

print("Accepted battery:", reading)

# Countdown
count = 10

while count >= 1:
    print(count)
    count -= 1

print("Lift off!")

# Sum numbers from 1 to 100
total = 0
number = 1

while number <= 100:
    total += number
    number += 1

print("Total from 1 to 100:", total)