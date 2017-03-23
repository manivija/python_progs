import subprocess, re, sys, os, time, datetime
# idea from https://gist.github.com/cwchiu/e2489a1430b420583c91

SEARCH_NAME = 'Roaming\Ansys\v181\SolveHandlers.xml'

def findOpenHandles(name):
	output = subprocess.check_output(['handle', name]).decode('utf-8')

	handles = set()
	for line in output.splitlines():
		if -1 == line.find(':'):
			continue
		parts = line.split(maxsplit=6)
		handles.add((parts[0], parts[2], parts[6]))

	return handles

while True:
	handles = findOpenHandles(SEARCH_NAME)
	if len(handles) != 0:
		print(datetime.datetime.now())
		for v in handles:
			print('\t'.join(v))
		break
	time.sleep(0.1)

# input('Press <Enter> to exit')
