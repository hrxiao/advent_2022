tree_grid = []
visible_grid = []
width = 0

with open("day8_input.txt") as f:
	for line in f:
		line = line.strip()
		trees = [int(tree) for tree in line]
		width = len(trees)
		tree_grid.append(trees)

		visible = [0] * width
		visible[0] = 1
		visible[-1] = 1
		tallest_left = trees[0]
		tallest_right = trees[-1]
		for i in range(1, width - 1):
			if trees[i] > tallest_left:
				tallest_left = trees[i]
				visible[i] = 1 

			if trees[width - i - 1] > tallest_right:
				tallest_right = trees[width - i - 1]
				visible[width - i - 1] = 1

		visible_grid.append(visible)

height = len(tree_grid)
visible_grid[0] = [1] * width
visible_grid[-1] = [1] * width

for col in range(width):
	tallest_top = tree_grid[0][col]
	tallest_bot = tree_grid[-1][col]
	for row in range(1, height - 1):
		if tree_grid[row][col] > tallest_top:
			tallest_top = tree_grid[row][col]
			visible_grid[row][col] = 1

		if tree_grid[height - row - 1][col] > tallest_bot:
			tallest_bot = tree_grid[height - row - 1][col]
			visible_grid[height - row - 1][col] = 1

print(f"num_visible={sum([sum(visible) for visible in visible_grid])}")

top_scene_score = 0
for row in range(1, height - 1):
	for col in range(1, width - 1):
		curr = tree_grid[row][col]
		# up
		up = 0
		r = row - 1
		while r >= 0:
			tree = tree_grid[r][col]
			up += 1
			r -= 1
			if tree >= curr:
				break
		# down
		down = 0
		r = row + 1
		while r < height:
			tree = tree_grid[r][col]
			down += 1
			r += 1
			if tree >= curr:
				break
		# left
		left = 0
		c = col - 1
		while c >= 0:
			tree = tree_grid[row][c]
			left += 1
			c -= 1
			if tree >= curr:
				break
		# right
		right = 0
		c = col + 1
		while c < width:
			tree = tree_grid[row][c]
			right += 1
			c += 1
			if tree >= curr:
				break

		scene = up * down * left * right
		# print(f"{row=} {col=} {up=} {down=} {left=} {right=} {scene=}")

		if scene > top_scene_score:
			top_scene_score = scene
print(f"{top_scene_score=}")

