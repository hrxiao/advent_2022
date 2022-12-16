valves = {}
valve_names = set()

def make_valve(line):
	line = line.strip().split()
	valve = {
		"name": line[1],
		"rate": int(line[4][5:-1]),
		"tunnels": [v.strip(",") for v in line[9:]],
		"index": -1,
	}
	return valve

# with open("day16_sample.txt") as f:
with open("day16_input.txt") as f:
	for line in f:
		valve = make_valve(line)
		valves[valve["name"]] = valve
		valve_names.add(valve["name"])

def make_dist_matrix(valves, valve_names):
	valve_names_list = sorted(list(valve_names))
	for i in range(len(valve_names)):
		valves[valve_names_list[i]]["index"] = i
	dist_matrix = [[-1] * len(valve_names) for _ in range(len(valve_names))]
	for valve in valves.values():
		dist_matrix[valve["index"]][valve["index"]] = 0

	for start_node in valves.keys():
		start_valve = valves[start_node]
		not_visited = set(valves.keys())
		to_visits = set(valves[start_node]["tunnels"])
		step = 0
		not_visited.remove(start_node)
		while len(not_visited) > 0:
			# print(f"{not_visited=}")
			# print(f"{to_visits=}\n")
			step += 1
			next_visits = set()
			for to_visit in to_visits:
				visiting = valves[to_visit]
				dist_matrix[start_valve["index"]][visiting["index"]] = step
				dist_matrix[visiting["index"]][start_valve["index"]] = step
				not_visited.remove(to_visit)
				for visit_tunnel in visiting["tunnels"]:
					if visit_tunnel in not_visited and visit_tunnel not in to_visits:
						next_visits.add(visit_tunnel)

			to_visits = next_visits
	return dist_matrix

def print_matrix(matrix):
	valve_names_list = sorted(list(valve_names))
	to_print = [" "]
	to_print.extend(valve_names_list)
	print(to_print)
	for i in range(len(matrix)):
		to_print = [valve_names_list[i]]
		to_print.extend(matrix[i])
		print(to_print)

dist_matrix = make_dist_matrix(valves, valve_names)
print_matrix(dist_matrix)

valves_by_rate = sorted(list(valves.values()), key=lambda valve: valve["rate"], reverse=True)
print(valves_by_rate)


minutes = 30
start = "AA"
