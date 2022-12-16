AIR = 0
SAND = 1
ROCK = 2

rock_lines = []
min_x = 1000
max_x = -1
max_y = -1

def to_xy(line):
	x,y = line.split(",")
	return (int(x), int(y))

def to_col(x):
	return x - min_x

def to_rc(rock_line):
	left, right = rock_line
	return ((to_col(left[0]), left[1]), (to_col(right[0]), right[1]))

def make_cave(rock_lines):
	cave = [[AIR] * (max_x - min_x + 1) for _ in range(max_y + 1)]
	for rock_line in rock_lines:
		left, right = to_rc(rock_line)
		if left[1] == right[1]:
			for i in range(abs(left[0] - right[0]) + 1):
				c = left[0] + (i * (1 if left[0] <= right[0] else -1))
				cave[left[1]][c] = ROCK
		else:
			for i in range(abs(left[1] - right[1]) + 1):
				r = left[1] + (i * (1 if left[1] <= right[1] else -1))
				cave[r][left[0]] = ROCK
	return cave

def print_cave(cave):
	for row in cave:
		out = ""
		for space in row:
			if space == AIR:
				out += "."
			elif space == SAND:
				out += "o"
			elif space == ROCK:
				out += "█"
		print(out)
	print("\n")

def pour_sand(cave):
	sand_start = (0, 500 - min_x)
	num_sand = 0
	while True:
		sand_r, sand_c = sand_start
		while True:
			if sand_r + 1 >= len(cave):
				print_cave(cave)
				return num_sand
			elif cave[sand_r + 1][sand_c] == AIR:
				sand_r += 1
			elif sand_c - 1 < 0:
				print_cave(cave)
				return num_sand
			elif cave[sand_r + 1][sand_c - 1] == AIR:
				sand_r += 1
				sand_c -= 1
			elif sand_c + 1 >= len(cave[0]):
				print_cave(cave)
				return num_sand
			elif cave[sand_r + 1][sand_c + 1] == AIR:
				sand_r += 1
				sand_c += 1
			else:
				cave[sand_r][sand_c] = SAND
				num_sand += 1
				break

def fill_sand(cave):
	num_sand = 0
	cave.append([AIR] * len(cave[0]))
	for r in range(len(cave)):
		row = cave[r]
		c_start = to_col(500 - r)
		c_end = to_col(500 + r)
		for c_idx in range(c_start, c_end + 1):
			if c_idx < 0 or c_idx >= len(row):
				num_sand += 1
			elif row[c_idx] != ROCK:
				num_sand += 1
				cave[r][c_idx] = SAND
			elif r != len(cave) - 1 and c_idx > 0 and row[c_idx - 1] == ROCK and c_idx < len(row) - 1 and row[c_idx + 1] == ROCK:
				cave[r+1][c_idx] = ROCK
	return num_sand


with open("day14_input.txt") as f:
	for line in f:
		lines = line.strip().split(" -> ")
		for i in range(len(lines) - 1):
			left = to_xy(lines[i])
			right = to_xy(lines[i+1])
			min_x = min(left[0], right[0]) if min_x > min(left[0], right[0]) else min_x
			max_x = max(left[0], right[0]) if max_x < max(left[0], right[0]) else max_x
			max_y = max(left[1], right[1]) if max_y < max(left[1], right[1]) else max_y
			rock_lines.append((left, right))



cave = make_cave(rock_lines)
print(f"max_sand={pour_sand(cave)}")
print(f"max_sand_fill={fill_sand(cave)}")

