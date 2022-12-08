from collections import defaultdict

class File:
	def __init__(self, name="", size=0, parent=None):
		self.name = name
		self.files = defaultdict(File)
		self.dirs = defaultdict(File)
		self.parent = parent
		self.size = size
		self.size_updated = False

	def get_parent(self):
		return self.parent

	def get_size(self):
		return self.size

	def get_dirs(self):
		return self.dirs.values()

	def visited(self):
		return self.size_updated

	def add_file(self, name, size):
		new_file = File(name, size)
		self.files[name] = new_file

	def add_dir(self, name):
		new_dir = File(name, 0, self)
		self.dirs[name] = new_dir

	def get_dir(self,name):
		if name not in self.dirs:
			self.add_dir(name)
		return self.dirs[name]

	def update_size(self):
		for f in self.files.values():
			self.size += f.get_size()
		for d in self.dirs.values():
			self.size += d.get_size()
		self.size_updated = True

root = File("/")

with open("day7_input.txt") as f:
	curr_dir = root
	for line in f:
		tokens = line.strip().split()
		if tokens[0] == "$":
			if tokens[1] == "cd":
				path = tokens[2]
				if path == "/":
					curr_dir = root
				elif path == "..":
					curr_dir = curr_dir.get_parent()
				else:
					curr_dir = curr_dir.get_dir(path)
		else:
			if tokens[0] == "dir":
				curr_dir.add_dir(tokens[1])
			else:
				curr_dir.add_file(tokens[1], int(tokens[0]))

def update_dir_size(root):
	threshold_size = 0
	to_visits = [root]
	while len(to_visits) > 0:
		curr_dir = to_visits.pop()
		children = list(curr_dir.get_dirs())
		if len(children) > 0 and not children[0].visited():
			to_visits.append(curr_dir)
			to_visits.extend(children)
		else:
			curr_dir.update_size()
			if curr_dir.get_size() <= 100000:
				threshold_size += curr_dir.get_size()
	return threshold_size

print(f"total_size={update_dir_size(root)}")

def min_delete_dir_size(root):
	threshold = root.get_size() - 40000000
	min_size = None
	to_visits = [root]
	while len(to_visits) > 0:
		curr_dir = to_visits.pop()
		curr_size = curr_dir.get_size()
		if curr_size > threshold:
			if min_size == None or curr_size < min_size:
				min_size = curr_size
			to_visits.extend(curr_dir.get_dirs())
	return min_size

print(f"min_delete_dir_size={min_delete_dir_size(root)}")