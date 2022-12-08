import re

stacks1 = [[] for _ in range(9)]
stacks2 = [[] for _ in range(9)]

def add_line(stacks, line):
	line = line.rstrip()
	column = 0
	idx = 0
	while idx < len(line):
		if line[idx] == "[":
			stacks[column].append(line[idx+1])
		idx += 4
		column += 1
	return stacks

def move_crates(stacks, num_crates, src, dst):
	for _ in range(num_crates):
		stacks[dst - 1].insert(0, stacks[src - 1].pop(0))
	return stacks

def move_crates_bulk(stacks, num_crates, src, dst):
	new_stack = stacks[src - 1][:num_crates]
	new_stack.extend(stacks[dst - 1])
	stacks[dst - 1] = new_stack
	stacks[src - 1] = stacks[src - 1][num_crates:]
	return stacks

def get_top_crates(stacks):
	top_crates = ""
	for stack in stacks:
		if len(stack) > 0:
			top_crates += stack[0]
	return top_crates

with open("day5_input.txt") as f:
	for line in f:
		if line.find("[") != -1:
			stacks1 = add_line(stacks1, line)
			stacks2 = add_line(stacks2, line)
		elif line.find("move") != -1:
			num_crates, src, dst = [int(x) for x in re.findall("\d+", line.strip())]
			stacks1 = move_crates(stacks1, num_crates, src, dst)
			stacks2 = move_crates_bulk(stacks2, num_crates, src, dst)

print(f"top_crates={get_top_crates(stacks1)}")
print(f"top_crates_bulk={get_top_crates(stacks2)}")
