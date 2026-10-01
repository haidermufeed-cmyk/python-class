raw_data = "Rover Alpha"
print(f"[{raw_data}]")
print(f"[{raw_data.strip()}]")
print(raw_data.strip().lower())
print(raw_data.strip().upper())
print(raw_data.strip().replace(" ", "_"))
print("Alpha" in raw_data)

# Sensor packet
packet = "TEMP:27;HUM:58;BAT:82"

parts = packet.split(";")

for item in parts:
    key, value = item.split(":")
    print(key, "=>", float(value))

# Custom robot packet
robot_info = "speed:4.5;gps:12,45;motor:0.8"

items = robot_info.split(";")

for item in items:
    key, value = item.split(":")
    print(key, "=>", value)