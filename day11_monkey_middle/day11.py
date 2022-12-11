import copy
import re

class Monkey:
	def __init__(self, args):
		self.items = args["items"]
		self.op = args["op"]
		self.op1 = args["op1"]
		self.op2 = args["op2"]
		self.test_div = args["test_div"]
		self.true_monkey = args["true_monkey"]
		self.false_monkey = args["false_monkey"]
		self.inspected = 0

	def num_inspected(self):
		return self.inspected

	def inspect(self, part2=None):
		monkey_pair = {self.true_monkey: [], self.false_monkey: []}
		for item in self.items:
			new_worry = int(self.op1) if self.op1 != "old" else item
			if self.op == "+":
				new_worry += int(self.op2) if self.op2 != "old" else item
			elif self.op == "*":
				new_worry *= int(self.op2) if self.op2 != "old" else item
			if part2:
				new_worry = new_worry % part2
			else:
				new_worry = new_worry // 3
			monkey_pair[self.true_monkey if (new_worry % self.test_div == 0) else self.false_monkey].append(new_worry)

		self.inspected += len(self.items)
		self.items = []
		return monkey_pair

	def catch(self, items):
		self.items.extend(items)

monkeys = []
MONKEY_ARGS = {
	"items": None,
	"op": None,
	"op1": None,
	"op2": None,
	"test_div": None,
	"true_monkey": None,
	"false_monkey": None
}

monkey_args = None
test_div_product = 1

# with open("day11_sample.txt") as f:
with open("day11_input.txt") as f:
	for line in f:
		line = line.strip()
		if line.find("Monkey") != -1:
			monkey_args = copy.deepcopy(MONKEY_ARGS)
		elif line.find("Starting") != -1:
			monkey_args["items"] = [int(x) for x in re.findall(r"\d+", line)]
		elif line.find("Operation") != -1:
			line = line[line.find("=") + 1:]
			op1, op, op2 = line.split()
			monkey_args["op"] = op
			monkey_args["op1"] = op1
			monkey_args["op2"] = op2
		elif line.find("Test") != -1:
			monkey_args["test_div"] = int(re.findall(r"\d+", line)[0])
			test_div_product *= monkey_args["test_div"]
		elif line.find("If true") != -1:
			monkey_args["true_monkey"] = int(re.findall(r"\d+", line)[0])
		elif line.find("If false") != -1:
			monkey_args["false_monkey"] = int(re.findall(r"\d+", line)[0])
			monkey = Monkey(monkey_args)
			monkeys.append(monkey)

monkeys1 = copy.deepcopy(monkeys)
for _ in range(20):
	for i in range(len(monkeys1)):
		monkey_pairs = monkeys1[i].inspect()
		for key, val in monkey_pairs.items():
			monkeys1[key].catch(val)

monkeys1.sort(key=lambda monkey: monkey.num_inspected(), reverse=True)
print(f"monkey_business={monkeys1[0].num_inspected() * monkeys1[1].num_inspected()}")

for _ in range(10000):
	for i in range(len(monkeys)):
		monkey_pairs = monkeys[i].inspect(test_div_product)
		for key, val in monkey_pairs.items():
			monkeys[key].catch(val)

monkeys.sort(key=lambda monkey: monkey.num_inspected(), reverse=True)
print(f"monkey_business2={monkeys[0].num_inspected() * monkeys[1].num_inspected()}")

