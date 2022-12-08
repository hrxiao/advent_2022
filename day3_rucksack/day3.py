sum_dup = 0
sum_badge = 0
badge_group = set()
i = 0

with open("day3_input.txt") as f:
	for line in f:
		items = list(line.strip())
		i1 = set(items[:len(items) // 2])
		i2 = set(items[len(items) // 2:])
		dup = list(i1.intersection(i2))[0]
		if dup.islower():
			sum_dup += (ord(dup) - ord('a')) + 1
		else:
			sum_dup += (ord(dup) - ord('A')) + 27

		if i == 0:
			badge_group = set(items)
		else:
			badge_group = badge_group.intersection(set(items))
		if i == 2:
			badge = list(badge_group)[0]
			if badge.islower():
				sum_badge += (ord(badge) - ord('a')) + 1
			else:
				sum_badge += (ord(badge) - ord('A')) + 27
		i = (i + 1) % 3

print(f"{sum_dup=} {sum_badge=}")