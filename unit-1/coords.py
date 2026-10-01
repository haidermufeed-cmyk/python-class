visited_cells = {(0, 0), (1, 0)}

visited_cells.add((2, 1))
visited_cells.add((0, 0))

print("Visited cells:", visited_cells)
print("Total distinct cells:", len(visited_cells))
print("(2, 1) visited?", (2, 1) in visited_cells)
print("(8, 8) visited?", (8, 8) in visited_cells)

# Removing duplicates with a set
error_codes = ["E4", "E9", "E4", "E2", "E9"]

print("All codes:", error_codes)
print("Different codes:", set(error_codes))
print("Number of different codes:", len(set(error_codes)))

# Tuple coordinates
location = (6.5, 3.2)

print("Location:", location)
print("Type:", type(location))

x_coord, y_coord = location
print("X =", x_coord, "| Y =", y_coord)

single_value = (8,)
print("Single-item tuple:", single_value)
print("Type:", type(single_value))

# Robot grid visit simulation
cells = set()

cells.add((0, 0))
cells.add((0, 1))
cells.add((1, 1))
cells.add((2, 2))
cells.add((2, 2))
cells.add((3, 1))
cells.add((3, 2))
cells.add((4, 0))

print("Visited:", cells)
print("Distinct cells:", len(cells))
print("(2, 2) visited?", (2, 2) in cells)