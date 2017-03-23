import os
import stat
import threading


 threading.Timer(5.0, printit).start()
  print "Hello, World!"

printit()

input('Press <Enter> to exit')



import os
import stat
import threading

def printit():
	threading.Timer(5.0, printit).start()
	filepath = "C:/Users/vmanicka/AppData/Roaming/Ansys/v181/SolveHandlers.xml"
	st = os.stat(filepath)
	if bool(st.st_mode & stat.S_IRGRP) == True:
		if os.access(filepath, os.R_OK):
			print("Access is good!")

printit()