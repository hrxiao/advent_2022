def start_packet(line, distinct_chars):
	buffer = line[:distinct_chars]
	for i in range(distinct_chars, len(line)):
		if len(set(buffer)) == distinct_chars:
			return i
		buffer = buffer[1:]
		buffer += line[i]

with open("day6_input.txt") as f:
	for line in f:
		line = line.strip()
		print(f"start_packet={start_packet(line, 4)}")
		print(f"start_message={start_packet(line, 14)}")
