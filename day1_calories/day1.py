curr = 0
max_three = [0, 0 ,0]

with open("day1_input.txt") as f:
	for line in f:
		line = line.strip()
		if line == "":
			if curr > max_three[0]:
				max_three[0] = curr
				max_three.sort()
			curr = 0
		else:
			curr += int(line)

print(f"max={max_three[-1]}, max3={sum(max_three)}")