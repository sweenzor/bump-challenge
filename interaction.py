import subprocess

logs = open('bump1.log')
lines = logs.readlines()
logs.close()

print len(lines)

proc = subprocess.Popen('python bump-json.py', 
                        shell=True,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        )

#print '\n'.join(lines)
#(out, err) = proc.communicate('\n'.join(lines))

proc.stdin.writelines(lines[0:10] + ["\n"])
out = proc.stdout.read()
print out


#for i in lines:
#    print "INPUT: " + i
#    (out, err) = proc.communicate(i)
#    output = out.readline()
#    print "OUTPUT: " + output.rstrip()

#print remainder[0]
#print remainder[1]

