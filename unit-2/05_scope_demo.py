value = 10

def local_change():
    value = 50
    value += 5
    return value

print(local_change())
print(local_change())
print("Outside value:", value)


LIMIT = 75

def check_limit(number):
    return number >= LIMIT

print(check_limit(82))
print(check_limit(64))


total = 5

def increase():
    return total + 1

print("Without changing global:", increase())
print("Total remains:", total)


score = 0

def update_score():
    global score
    score += 10
    return score

print(update_score())
print(update_score())
print(update_score())
print("Final score:", score)


def next_value(current):
    return current + 1

counter = 0
counter = next_value(counter)
counter = next_value(counter)
counter = next_value(counter)

print("Counter:", counter)


def create_list():
    records = ["start"]
    records.append("finish")
    records.append("complete")
    return len(records)

print("Records:", create_list())
print("Records:", create_list())
print("records exists globally:", "records" in globals())