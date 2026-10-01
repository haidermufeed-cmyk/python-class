robot_name = "RoboMax"
battery_level = 42.5
is_docked = False
waypoints = 18

print("Robot Name:", robot_name)
print("Battery Level:", battery_level)
print("Docked:", is_docked)
print("Waypoints:", waypoints)

print("--- Data Types ---")
print(type(robot_name))
print(type(battery_level))
print(type(is_docked))
print(type(waypoints))

battery = 100
print("--- Battery Test ---")
print("Starting battery:", battery)

battery = battery - 20
print("After first drain:", battery)

battery -= 15
print("After second drain:", battery)

print("--- Status Check ---")
if battery_level < 50:
    print("WARNING: Battery level is low")
    print("Robot should return for charging.")

print("Robot status check complete.")