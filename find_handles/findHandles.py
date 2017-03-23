import subprocess, re, sys, os, time, datetime
# idea from https://gist.github.com/cwchiu/e2489a1430b420583c91

# SEARCH_NAME = 'Ansys\v181'
SEARCH_NAME = 'Roaming\Ansys\v181\SolveHandlers.xml'
HANDLE_EXE = os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), 'Handle', 'Handle.exe')

def findOpenHandles(name):
	output = subprocess.check_output([HANDLE_EXE, name]).decode('utf-8')

	handles = set()
	for line in output.splitlines():
		if -1 == line.find(':'):
			continue
		parts = line.split(maxsplit=6)
		handles.add((parts[0], parts[2], parts[6]))

	return handles

start = time.time()
def hasBeen24Hours():
	return 60*60*24 <= (time.time() - start)

while True:
	if hasBeen24Hours():
		break

	handles = findOpenHandles(SEARCH_NAME)
	if len(handles) != 0:
		print(datetime.datetime.now())
		for v in handles:
			print('\t'.join(v))
	time.sleep(0.1)

# input('Press <Enter> to exit')
