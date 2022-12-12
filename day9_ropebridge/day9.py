class Rope:
	def __init__(self, length):
		self.knots_x = [0] * length
		self.knots_y = [0] * length
		self.visited = set()
		self.add_visited()

	def get_visited(self):
		return len(self.visited)

	def add_visited(self):
		self.visited.add((self.knots_x[-1], self.knots_y[-1]))

	def move_head(self, direction):
		if direction == "U":
			self.knots_y[0] += 1
		elif direction == "D":
			self.knots_y[0] -= 1
		elif direction == "L":
			self.knots_x[0] -= 1
		else:
			self.knots_x[0] += 1

		self.move_knot(1)

	def move_knot(self, i):
		x_diff = abs(self.knots_x[i] - self.knots_x[i - 1])
		y_diff = abs(self.knots_y[i] - self.knots_y[i - 1])

		# 1 away x or y
		if x_diff + y_diff < 2:
			return
		# 2 away diagonal
		if x_diff + y_diff > 2:
			self.knots_x[i] += 1 if self.knots_x[i-1] > self.knots_x[i] else -1
			self.knots_y[i] += 1 if self.knots_y[i-1] > self.knots_y[i] else -1
		else:
			# 2 away y
			if x_diff == 0:
				self.knots_y[i] += 1 if self.knots_y[i-1] > self.knots_y[i] else -1
			# 2 away x
			elif y_diff == 0:
				self.knots_x[i] += 1 if self.knots_x[i-1] > self.knots_x[i] else -1
			else:
				return

		if i == len(self.knots_x) - 1:
			self.add_visited()
		else:
			self.move_knot(i + 1)

short_rope = Rope(2)
long_rope = Rope(10)

with open("day9_input.txt") as f:
	for line in f:
		direction, steps = line.strip().split()
		steps = int(steps)
		for _ in range(steps):
			short_rope.move_head(direction)
			long_rope.move_head(direction)

print(f"short tail visited={short_rope.get_visited()}")
print(f"long tail visited={long_rope.get_visited()}")
