def summarize(data):
    average = sum(data) / len(data)
    smallest = min(data)
    largest = max(data)
    return average, smallest, largest


measurements = [18.4, 21.7, 19.2, 25.3, 20.6]

result = summarize(measurements)
result = list(result)

print("Statistics:", result)
print("Type:", type(result))


def welcome(robot):
    print("Welcome", robot)


answer = welcome("Rover-A")
print("Returned value:", answer)
print("Returned type:", type(answer))


def divide_numbers(x, y):
    if y == 0:
        return None
    return x / y


print("Result:", divide_numbers(20, 4))
print("Result:", divide_numbers(20, 0))


def insert_value(values, new_value):
    values.append(new_value)


sensor_values = [12, 18]
insert_value(sensor_values, 25)

print("After function:", sensor_values)


def replace_list(values):
    values = [100]
    return values


original_values = [12, 18]
replace_list(original_values)

print("Original list:", original_values)


def calculate_path(coordinates):
    distance = 0

    for index in range(len(coordinates) - 1):
        x1, y1 = coordinates[index]
        x2, y2 = coordinates[index + 1]

        dx = x2 - x1
        dy = y2 - y1

        distance += (dx ** 2 + dy ** 2) ** 0.5

    return distance


path_length = calculate_path([(1, 1), (4, 5)])

print("Path length:", path_length)
print("Can calculate further?", path_length + 2 if path_length is not None else "No value")