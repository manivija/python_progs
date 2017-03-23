import subprocess, re, time, os, sys

# os.system("ex_2.py Roaming\Ansys\v181")

#p = subprocess.run(['ex_2.py', 'Roaming\Ansys\v181'], stdout=subprocess.PIPE)
p = subprocess.Popen(['ex_2.py', 'Roaming\Ansys\v181'], stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
p_status = p.wait()
print (output.decode("utf-8"))
input('Press <Enter> to exit')

# timeout = time.time() + 60*5   # 5 minutes from now
# while True:
    # if time.time() > timeout:
        # break

	# time.sleep(10)