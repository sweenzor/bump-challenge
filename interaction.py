import subprocess

logs = open('postmap1.log')
lines = logs.readlines()


proc = subprocess.Popen('python bump-reducer.py', 
                        shell=True,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        )

for i in lines:
    proc.stdin.write(i)
    #output = proc.stdout.readline()
    #print output.rstrip()

remainder = proc.communicate()[0]
print remainder

