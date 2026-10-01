def save_waypoint(point, path=None):
    if path is None:
        path = []

    path.append(point)
    return path


first_path = save_waypoint((2, 1))
second_path = save_waypoint((6, 4))

print("first_path =", first_path)
print("second_path =", second_path)
print("same object?", first_path is second_path)