heading = 275
rotation = 110

print("Normal result:", heading + rotation)
print("Wrapped result:", (heading + rotation) % 360)
print("Negative angle:", (-45) % 360)

distance = 7.5
safe_limit = 12

print(distance < safe_limit)
print(distance == safe_limit)
print(0 <= distance < safe_limit)

battery = 65

print(distance > 5 and battery > 30)
print(distance > 5 or battery < 20)
print(distance > 5)

# Robot movement safety check
distance = 25
battery = 60
is_docked = False

safe_to_move = distance > 10 and battery > 20 and not is_docked

print("Safe to move:", safe_to_move)