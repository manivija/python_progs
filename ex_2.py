import subprocess, re, sys, os
HANDLE_EXE = 'handle'

# idea from https://gist.github.com/cwchiu/e2489a1430b420583c91

for i,fn in enumerate(sys.argv): 
	if i == 0:
		continue

	# print fn
	output = subprocess.check_output([HANDLE_EXE, fn]).decode("utf-8")

	# handles = re.findall('(\S+)\s+ pid:\s+(\d+)\s+type: \w+\s+([0-9A-Z]+): ', output)
	#handles = re.findall('(\S+)\s+ pid:\s+(\d+)\s+type: \w+\s+[0-9A-Z]+:\s+(\S+)', output)
	# handles = re.findall('(\S+)\s+ pid:\s+(\d+)', output)
	
	handles = []
	for line in output.splitlines():
		if -1 == line.find(':'):
			continue
		parts = line.split(maxsplit=6)
		handles.append((parts[0], parts[2], parts[6]))

	handles = set(handles)
	for v in handles:
		print('\t'.join(v))

# input('Press <Enter> to exit')
