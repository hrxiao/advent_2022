grid = []
start = None
end = None

def should_visit(grid, visited, curr_r, curr_c, next_r, next_c):
	if next_r < 0 or next_r >= len(grid):
		return False
	if next_c < 0 or next_c >= len(grid[0]):
		return False
	if visited[next_r][next_c] != -1:
		return False
	if grid[next_r][next_c] > grid[curr_r][curr_c] + 1:
		return False
	return True

def climb(grid, start, end):
	visited = [ [-1] * len(grid[0]) for _ in range(len(grid))]
	to_visits = [(start[0], start[1], 0)]
	while True:
		(r, c, step) = to_visits.pop(0)
		if visited[r][c] != -1:
			continue
		if r == end[0] and c == end[1]:
			return step
		visited[r][c] = step
		if should_visit(grid, visited, r, c, r - 1, c):
			to_visits.append((r - 1, c, step + 1))
		if should_visit(grid, visited, r, c, r + 1, c):
			to_visits.append((r + 1, c, step + 1))
		if should_visit(grid, visited, r, c, r, c - 1):
			to_visits.append((r, c - 1, step + 1))
		if should_visit(grid, visited, r, c, r, c + 1):
			to_visits.append((r, c + 1, step + 1))

def should_visit_down(grid, visited, curr_r, curr_c, next_r, next_c):
	if next_r < 0 or next_r >= len(grid):
		return False
	if next_c < 0 or next_c >= len(grid[0]):
		return False
	if visited[next_r][next_c] != -1:
		return False
	if grid[next_r][next_c] < grid[curr_r][curr_c] - 1:
		return False
	return True

def climb_shortest(grid, start):
	visited = [ [-1] * len(grid[0]) for _ in range(len(grid))]
	to_visits = [(start[0], start[1], 0)]
	while True:
		(r, c, step) = to_visits.pop(0)
		if visited[r][c] != -1:
			continue
		if grid[r][c] == 0:
			return step
		visited[r][c] = step
		if should_visit_down(grid, visited, r, c, r - 1, c):
			to_visits.append((r - 1, c, step + 1))
		if should_visit_down(grid, visited, r, c, r + 1, c):
			to_visits.append((r + 1, c, step + 1))
		if should_visit_down(grid, visited, r, c, r, c - 1):
			to_visits.append((r, c - 1, step + 1))
		if should_visit_down(grid, visited, r, c, r, c + 1):
			to_visits.append((r, c + 1, step + 1))

# with open("day12_sample.txt") as f:
with open("day12_input.txt") as f:
	r = 0
	for line in f:
		line = line.strip()
		row = []
		c = 0
		for x in line:
			if x == 'S':
				start = (r, c)
				x = 'a'
			elif x == 'E':
				end = (r, c)
				x = 'z'
			row.append(ord(x) - ord('a'))
			c += 1
		grid.append(row)
		r += 1

print(f"steps={climb(grid, start, end)}")
print(f"shortest_steps={climb_shortest(grid, end)}")
