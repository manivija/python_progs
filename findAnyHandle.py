import subprocess, re, sys, os
# idea from https://gist.github.com/cwchiu/e2489a1430b420583c91

HANDLE_EXE = 'handle'
# the location of handle.exe or add handle.exe path to the path variable in the environment variables and use 'handle'
# HANDLE_EXE = os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])),'Dependencies', 'Handle', 'handle.exe')

for i,fn in enumerate(sys.argv): 
	if i == 0:
		continue

	output = subprocess.check_output([HANDLE_EXE, fn]).decode("utf-8")

	# handles = re.findall('(\S+)\s+ pid:\s+(\d+)\s+type: \w+\s+([0-9A-Z]+): ', output)
	handles = re.findall('(\S+)\s+ pid:\s+(\d+)\s+type: \w+\s+[0-9A-Z]+:\s+(.*)', output)
	# handles = re.findall('(\S+)\s+ pid:\s+(\d+)', output)

	handles = set(handles)

	for v in handles:
		print('\t'.join(v))

# input('Press <Enter> to exit')
