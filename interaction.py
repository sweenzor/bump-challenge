import subprocess

logs = open('postmap2.log')
lines = logs.readlines()
logs.close()

proc = subprocess.Popen('python bump-reducer.py', 
                        shell=True,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        )

#print '\n'.join(lines)
#(out, err) = proc.communicate('\n'.join(lines))

proc.stdin.writelines(lines[0:3500] + ["\n"])
out = proc.stdout.read()
print out


#for i in lines:
#    print "INPUT: " + i
#    (out, err) = proc.communicate(i)
#    output = out.readline()
#    print "OUTPUT: " + output.rstrip()

#print remainder[0]
#print remainder[1]

