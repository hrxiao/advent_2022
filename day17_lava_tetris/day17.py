# NUM_ROCKS = 2022
NUM_ROCKS = 1000000000000
winds = []
chamber = [[0] * 10000 for _ in range(7)]
for col in chamber:
	col[0] = 1

# with open("day17_sample.txt") as f:
with open("day17_input.txt") as f:
	for line in f:
		winds = list(line.strip())

def get_wind(iter):
	return winds[iter % len(winds)]

def get_rock(rock_num, height):
	choice = rock_num % 5
	if choice == 0:
		return [(2, height + 4), (3, height + 4), (4, height + 4), (5, height + 4)]
	elif choice == 1:
		return [(3, height + 4), (2, height + 5), (3, height + 5), (4, height + 5), (3, height + 6)]
	elif choice == 2:
		return [(2, height + 4), (3, height + 4), (4, height + 4), (4, height + 5), (4, height + 6)]
	elif choice == 3:
		return [(2, height + 4), (2, height + 5), (2, height + 6), (2, height + 7)]
	elif choice == 4:
		return [(2, height + 4), (3, height + 4), (2, height + 5), (3, height + 5)] 

def push_rock(rock, wind):
	if wind == "<":
		return [(x - 1, y) for (x, y) in rock]
	return [(x + 1, y) for (x, y) in rock]

def fall_rock(rock):
	return [(x, y - 1) for (x, y) in rock]

def is_collision(chamber, rock):
	for (x, y) in rock:
		if x < 0 or x > 6:
			return True
		if chamber[x][y] == 1:
			return True
	return False

def rest_rock(chamber, rock):
	for (x, y) in rock:
		chamber[x][y] = 1
	return chamber

def to_key(chamber, wind_num, rock_num, y):
	out = ""
	for col in chamber:
		out += str(col[y-50:y+1])		
	return (rock_num % 5, wind_num % len(winds), out)

def update_height(curr_height, rock):
	for (x, y) in rock:
		if y > curr_height:
			curr_height = y
	return curr_height

def print_chamber(chamber, height):
	output = "|0123456|\n"
	for h in reversed(range(1, height + 1)):
		output += "|"
		for col in chamber:
			output += "." if col[h] == 0 else "#"
		output += "| " + str(h) +"\n"
	output += "|-------| 0\n|0123456|\n"
	print(output)

wind_num = 0
rock_num = 0
curr_height = 0
height_skipped = 0

# key = (rock piece num, wind index, top 30 rows)
# val = rock_num, height
patterns = {}

while rock_num < NUM_ROCKS:
	rock = get_rock(rock_num, curr_height)
	frame = 0
	while True:
		next_rock = None
		if frame % 2 == 0:
			next_rock = push_rock(rock, get_wind(wind_num))
			wind_num += 1
		else:
			next_rock = fall_rock(rock)
		if not is_collision(chamber, next_rock):
			rock = next_rock
		elif frame % 2:
			break
		frame += 1

	chamber = rest_rock(chamber, rock)
	curr_height = update_height(curr_height, rock)

	if rock_num > 50:
		curr_pattern = to_key(chamber, wind_num, rock_num, curr_height)
		if curr_pattern in patterns:
			(old_rock_num, old_height) = patterns[curr_pattern]
			cycle = rock_num - old_rock_num
			height_diff = curr_height - old_height

			cycles_to_skip = (NUM_ROCKS - rock_num) // cycle
			if cycles_to_skip > 1:
				height_skipped += height_diff * cycles_to_skip
				print(f"FOUND pattern at {rock_num=}")
				rock_num += cycles_to_skip * cycle
				print(f"Skip to {rock_num=}")
		else:
			patterns[curr_pattern] = (rock_num, curr_height)

	rock_num += 1

print(f"{curr_height=} {height_skipped=} total_height={curr_height + height_skipped}")