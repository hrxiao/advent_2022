from functools import lru_cache

valves = {}
valve_names = set()
good_valves = {}

def make_valve(line):
	line = line.strip().split()
	valve = {
		"name": line[1],
		"rate": int(line[4][5:-1]),
		"tunnels": [v.strip(",") for v in line[9:]],
	}
	return valve

# with open("day16_sample.txt") as f:
with open("day16_input.txt") as f:
	for line in f:
		valve = make_valve(line)
		valves[valve["name"]] = valve
		valve_names.add(valve["name"])
		if valve["rate"] > 0:
			good_valves[valve["name"]] = valve

# poor mans floyd warshall
def make_dist_map(valves, valve_names):
	dist_map = {}
	# start from each valve
	for start_node in valves.keys():
		# valve to itself is 2 steps
		dist_map[(start_node, start_node)] = 2
		not_visited = set(valves.keys())
		to_visits = set(valves[start_node]["tunnels"])
		step = 0
		not_visited.remove(start_node)
		while len(not_visited) > 0:
			step += 1
			next_visits = set()
			for to_visit in to_visits:
				visiting = valves[to_visit]
				dist_map[(start_node, to_visit)] = step			
				dist_map[(to_visit, start_node)] = step
				not_visited.remove(to_visit)
				for visit_tunnel in visiting["tunnels"]:
					if visit_tunnel in not_visited and visit_tunnel not in to_visits:
						next_visits.add(visit_tunnel)
			to_visits = next_visits
	return dist_map

dist_map = make_dist_map(valves, valve_names)


# Algorithm by
# https://topaz.github.io/paste/#XQAAAQDfAgAAAAAAAAA0m0pnuFI8c82uPD0wiI6r5tRTRja98xwzlfwFtjHHMXROBlAd++OM5E2aWHrlz38tgjgBrDMkBDPm5k7eRTLnCaSEUZUXANmWw6a7dmZdD+qaJFp7E26PQ9Ml4fpikPmCeDnULBn3YHI/yLHbVDEdzTxQZhxa+aFb3fX8qpx50mBxYGkYIvkYoHqoND3JEEe2PE8yfBjpZNgC+Vp30p9nwCUTCSQrDlaj6RCgZyoOK4E/0QTzzMTpAvuwXfRpaEG4N87Y0Rr49K516SKwkvAatNXD/MBZ2thEgjpndUPRb/SA5eo0d/OjeyIlhgFibQYYZ4KHpAn3uPUJ9CSsdyr6/TnmqI95UsPYgMPNLWjLQmy3+35ne8bKXq3SHASY+91H7LIAFMGp5QhI53Qkvfo+WAJDHW6OTabv0QXSAvP57DAnBBAMS+R0W4H3bc4fRaVa+nfP7ifAKLKxGr1w3jHedPV2HRQ4bLOdmkB0vO9OReM6lNK7nTH1EF91P5PwmenHxXGnjjhp12efsEpBwFP/p/Vk7z/7zxwFT7c5+MBovbAHfbFNxQZtnVlrS1cGvRmx5bufXqoglHIp7DFNWyZVPp8TE5qiC8hSEyzLr/+x2pjq

# recursively find the pressure by visiting all other valves and updating time
# remaining with the cost of visiting other valves
@lru_cache(maxsize=None)
def max_valve_pressure(curr_valve, time_left, unopened_valves, has_elephant):
	# check max with if elephant by itself is to visit the unopened valves
	max_pressure = 0 if not has_elephant else max_valve_pressure("AA", 26, unopened_valves, False)
	for unopened_valve in unopened_valves:
		time_to_valve = dist_map[(curr_valve, unopened_valve)]
		if time_to_valve >= time_left:
			continue
		new_time_left = time_left - 1 - time_to_valve
		pressure_from_valve = valves[unopened_valve]["rate"] * (time_left - 1 - time_to_valve)
		recurse_pressure = max_valve_pressure(unopened_valve, new_time_left, unopened_valves - {unopened_valve}, has_elephant)
		total_pressure = pressure_from_valve + recurse_pressure
		if total_pressure > max_pressure:
			max_pressure = total_pressure
	return max_pressure

print(f"max_valve_pressure={max_valve_pressure('AA', 30, frozenset(good_valves.keys()), False)}")
print(f"max_valve_pressure_duo={max_valve_pressure('AA', 26, frozenset(good_valves.keys()), True)}")
