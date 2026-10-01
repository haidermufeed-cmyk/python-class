def battery_status(level, robot="Rover"):
    if level < 20:
        print(f"{robot}: CRITICAL")
    elif level < 40:
        print(f"{robot}: LOW")
    else:
        print(f"{robot}: OK")


battery_status(14, "Rover-A")
battery_status(35, "Rover-B")
battery_status(82)


def battery_band(level):
    if level < 20:
        return "critical"
    elif level < 40:
        return "low"
    else:
        return "normal"


fleet = {
    "Rover-A": 14,
    "Rover-B": 35,
    "Rover-C": 82,
    "Rover-D": 57
}

for robot, level in fleet.items():
    print(f"{robot:<9} {level:>3}% {battery_band(level)}")


def circle_area(radius):
    return 3.14 * radius * radius


total_area = circle_area(4) + circle_area(6)
print("Combined area:", total_area)


def move_robot(x, y, speed=1.5):
    print(f"Moving to ({x}, {y}) at {speed} m/s")


move_robot(5, 2)
move_robot(5, 2, 0.8)
move_robot(y=2, x=5)
move_robot(5, speed=2.5, y=2)


def record_event(*events, **details):
    print("Events:", events)
    print("Details:", details)


record_event("start")
record_event("move", "scan", "return")
record_event("warning", level="high", attempts=3)
record_event()


def add_waypoint(point, route=None):
    if route is None:
        route = []

    route.append(point)
    return route


route_a = add_waypoint((1, 2))
route_b = add_waypoint((6, 7))

print("route_a =", route_a)
print("route_b =", route_b)
print("Same object?", route_a is route_b)