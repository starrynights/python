import sys
import fileinput

#type 1
#for line in sys.stdin:
#    print line

#type 2
#for line in fileinput.input(sys.argv[1]):
#    line = line.rstrip()
#    print line

#type 3
f = open(sys.argv[1])
for line in f:
    '''add , after print can del \n'''
    print line,
f.close()


