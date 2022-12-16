import re

sensors = []

def make_sensor(coords):
	x, y, b_x, b_y = coords
	return {
		"x": x,
		"y": y,
		"bx": b_x,
		"by": b_y,
		"d": abs(x - b_x) + abs(y - b_y)
	}

with open("day15_input.txt") as f:
	for line in f:
		sensors.append(make_sensor([int(i) for i in re.findall("-?\d+", line.strip())]))

def merge_ranges(ranges, x_bound):
	ranges.sort()
	out = [ranges[0]]
	for i in ranges[1:]:
		last_start, last_end = out[-1]
		start, end = i
		if x_bound is not None and start > x_bound:
			break
		if last_end < start:
			out.append(i)
		elif last_end == start:
			out[-1][1] = end
		elif last_end < end:
			out[-1][1] = end
		if x_bound is not None and out[-1][1] > x_bound:
			out[-1][1] = x_bound
			break
	return out

def not_beacon_range(sensors, y, x_bound=None):
	beacons = set()
	not_beacon_ranges = []
	for sensor in sensors:
		if sensor["by"] == y:
			beacons.add(sensor["bx"])
		dist_left = sensor["d"] - abs(sensor["y"] - y)
		if dist_left >= 0:
			not_beacon_ranges.append([sensor["x"] - dist_left, sensor["x"] + dist_left])
	return (merge_ranges(not_beacon_ranges, x_bound), beacons)

def count_not_beacon(sensors, y):
	y_range, y_beacons = not_beacon_range(sensors, y)
	count = 0
	for r in y_range:
		count += r[1] - r[0] + 1
		for beacon in y_beacons:
			if r[0] <= beacon <= r[1]:
				count -= 1
	return count

def find_distress_beacon(sensors, x_bound, y_bound):
	for y in range(y_bound, -1, -1):
		ranges = not_beacon_range(sensors, y, x_bound)[0]
		if len(ranges) > 1:
			x = ranges[0][1] + 1
			return x * 4000000 + y

print(f"not_beacons={count_not_beacon(sensors, 2000000)}")
print(f"frequency={find_distress_beacon(sensors, 4000000, 4000000)}")