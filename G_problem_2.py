
# Elevator Maintenance
# ====================

# You've been assigned the onerous task of elevator maintenance - ugh! It wouldn't be so bad, except that all the elevator documentation has been lying in a disorganized pile at the bottom of a filing cabinet for years, and you don't even know what elevator version numbers you'll be working on. 

# Elevator versions are represented by a series of numbers, divided up into major, minor and revision integers. New versions of an elevator increase the major number, e.g. 1, 2, 3, and so on. When new features are added to an elevator without being a complete new version, a second number named "minor" can be used to represent those new additions, e.g. 1.0, 1.1, 1.2, etc. Small fixes or maintenance work can be represented by a third number named "revision", e.g. 1.1.1, 1.1.2, 1.2.0, and so on. The number zero can be used as a major for pre-release versions of elevators, e.g. 0.1, 0.5, 0.9.2, etc (Commander Lambda is careful to always beta test her new technology, with her loyal henchmen as subjects!).

# Given a list of elevator versions represented as strings, write a function answer(l) that returns the same list sorted in ascending order by major, minor, and revision number so that you can identify the current elevator version. The versions in list l will always contain major numbers, but minor and revision numbers are optional. If the version contains a revision number, then it will also have a minor number.

# For example, given the list l as ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"], the function answer(l) would return the list ["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"]. If two or more versions are equivalent but one version contains more numbers than the others, then these versions must be sorted ascending based on how many numbers they have, e.g ["1", "1.0", "1.0.0"]. The number of elements in the list l will be at least 1 and will not exceed 100.

# Languages
# =========

# To provide a Python solution, edit solution.py
# To provide a Java solution, edit solution.java

# Test cases
# ==========

# Inputs:
    # (string list) l = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]
# Output:
    # (string list) ["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"]

# Inputs:
    # (string list) l = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
# Output:
    # (string list) ["0.1", "1.1.1", "1.2", "1.2.1", "1.11", "2", "2.0", "2.0.0"]

#input = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]
#input = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
#input = ["1.0.0", "1.0", "1.0"]
#input = ["2.12.0", "0.2.99", "2.5.0", "2.5.1", "2.0.1", "2.0", "2.0.0", "2","2.0","0.1.19", "1.19.18", "0.19", "0.19.10"]

def answer(input):

	maxEntrySize = max([ (max([len(v) for v in e.split(".")])) for e in input])

	def eval(str1, maxEntrySize):

		def compute(v, i, maxEntrySize, zeroCase):
			raised = maxEntrySize + i * 3
			if i == 0:
				if zeroCase:
					return (v - 0.1)/(10**raised)
				else:
					return v/(10**raised)
			else:
				return (v + 0.1)/(10**raised)

		stringIn = str1

		if int(stringIn.split(".")[0]) == 0:
			stringIn = str1[2:]
			return sum([compute(int(stringIn.split(".")[i]),i,maxEntrySize, True) for i in range(len(stringIn.split(".")))])
		else:
			return sum([compute(int(stringIn.split(".")[i]),i,maxEntrySize, False) for i in range(len(stringIn.split(".")))])

	return sorted(
		input,
		key = lambda elem: eval(elem, maxEntrySize)
	)

print(answer(input))