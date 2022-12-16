from ast import literal_eval

def in_order(left, right):
	if isinstance(left, list) and isinstance(right, list):
		i = 0
		while True:
			if i == len(left) and not i == len(right):
				return -1
			elif i == len(left) and i == len(right):
				return 0
			elif not i == len(left) and i == len(right):
				return 1
			else:
				rc = in_order(left[i], right[i])
				if rc != 0:
					return rc
			i += 1

	elif isinstance(left, int) and isinstance(right, int):
		if left == right:
			return 0
		return -1 if left < right else 1

	elif isinstance(left, list) and isinstance(right, int):
		rc = in_order(left, [right])
		if rc != 0:
			return rc

	else:
		rc = in_order([left], right)
		if rc != 0:
			return rc

	return 0

in_order_sum = 0
left = None
right = None
index = 1

divider1 = [[2]]
divider2 = [[6]]
div1_idx = 1
div2_idx = 2 # div1 < div2

with open("day13_input.txt") as f:
	for line in f:
		line = line.strip()
		if line == "":
			continue
		if left == None:
			left = literal_eval(line)
		elif right == None:
			right = literal_eval(line)
			if in_order(left, right) == -1:
				in_order_sum += index

			if in_order(divider1, left) == 1:
				div1_idx += 1
			if in_order(divider2, left) == 1:
				div2_idx += 1
			if in_order(divider1, right) == 1:
				div1_idx += 1
			if in_order(divider2, right) == 1:
				div2_idx += 1

			left = None
			right = None
			index += 1

print(f"{in_order_sum=} key={div1_idx*div2_idx}")