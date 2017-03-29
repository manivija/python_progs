items = [1,7,8,0,-1,2,-3]
# items = [0,0,0,0,0]
# items = [1,7,0,-1,2,-3,-8]
# items = [-3,-2,-4,-6,-8]
# items = [-3,-2,-4,-5]
# items = [3,2,4,5]

# sort items
items = sorted(items)
print(items)

def prod(list_ent):
	prodTotal = 1
	for e in list_ent:
		prodTotal *= e
	print(prodTotal)
	return prodTotal

prodList = []

for i in range(len(items)):
	if items[i] != 0 and len(items[0:i]):
		print([item for item in items[0:i+1] if item != 0])
		prodList.append(prod([item for item in items[0:i+1] if item != 0]))

print("Here!!")
print (prodList)
if len(prodList):
	if max(prodList) != prodList[len(prodList) - 1]:
		negaveItems = [item for item in items if item < 0]
		print(prodList[len(prodList) - 1]/negaveItems[len(negaveItems) - 1])
	else:
		print(max(prodList))
else:
	if len(items) > len(prodList):
		print(0)
	else:
		print ("error!")


#prodList = [ prod([items[j] for j in range(i) if items[j] != 0]) for i in range(len(items)) if items[i] != 0]