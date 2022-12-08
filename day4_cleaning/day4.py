def get_start_end(range):
	start_end = range.split("-")
	return (int(start_end[0]), int(start_end[1]))

complete_overlaps = 0
overlaps = 0

with open("day4_input.txt") as f:
	for line in f:
		ranges = line.strip().split(",")
		s1, e1 = get_start_end(ranges[0])
		s2, e2 = get_start_end(ranges[1])

		if (s1 <= s2 and e1 >= e2) or (s2 <= s1 and e2 >= e1):
			complete_overlaps += 1

		if not (e1 < s2 or e2 < s1):
			overlaps += 1

print(f"{complete_overlaps=} {overlaps=}")