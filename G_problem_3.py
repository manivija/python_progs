possibleInputs = [
	[1,7,8,0,-1,2,-3], [0,0,0,0,0], [7,0], [0,1], [0], [-2,0], [0,-2], [2,3], [-2,3],
	[1,7,0,-1,2,-3,-8], [-3,-2,-4,-6,-8], [-3,-2,-4,-5], [3,2,4,5], [-1,-1], [-2,0,1]
]

# possibleInputs = [
# 	[-3,-2,-4,-6,-8]
# ]

# sort items
def answer(items):

	if len(items) == 1:
		return str(items[0])

	items = sorted(items)

	def prod(list_ent):
		prodTotal = 1
		for e in list_ent:
			prodTotal *= e
		return prodTotal

	negativeList = [x for x in items if x < 0]
	if len(negativeList) > 1:
		if len(negativeList) % 2 != 0:
			negativeList = negativeList[: len(negativeList) - 1 ]
	else:
		negativeList = []

	positiveList = [x for x in items if x > 0]

	NetList = positiveList + negativeList
	if len(NetList) != 0:
		return str(prod(NetList))

	return str(0)

for xs in possibleInputs:
	print(str(xs))
	print(answer(xs))
	print("\n")

#prodList = [ prod([items[j] for j in range(i) if items[j] != 0]) for i in range(len(items)) if items[i] != 0]
