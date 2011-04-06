import subprocess

logs = open('bump10.log')
lines = logs.readlines()


for i in lines:
    proc = subprocess.Popen('python bump-json.py', 
                            shell=True,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            )

    proc.stdin.write('%s\n' % i)
    output = proc.stdout.readline()
    print output.rstrip()
remainder = proc.communicate()[0]
print remainder

