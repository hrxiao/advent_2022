
cycle = 0
register = 1
crt = [ [" "]*40 for _ in range(6)]
strengths = []

def print_crt(crt):
	for row in crt:
		print("".join(row))

def draw_pixel(cycle, register, crt):
	row = (cycle - 1) // 40
	col = (cycle - 1) % 40
	if abs(col - register) <= 1:
		crt[row][col] = "#"
	return crt


def clock(cycle, register, strengths, crt):
	cycle += 1
	if (cycle - 20) % 40 == 0:
		strengths.append(register * cycle)
	crt = draw_pixel(cycle, register, crt)
	return (cycle, strengths, crt)


with open("day10_input.txt") as f:
	for line in f:
		cycle, strengths, crt = clock(cycle, register, strengths, crt)
		tokens = line.strip().split()
		if len(tokens) == 2:
			cycle, strengths, crt = clock(cycle, register, strengths, crt)
			register += int(tokens[1])

print(f"sum_signl_strength={sum(strengths)}")
print_crt(crt)