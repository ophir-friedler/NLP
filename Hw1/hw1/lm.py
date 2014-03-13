'''
Created on Mar 13, 2014

@author: ophirf
'''

if __name__ == '__main__':
    pass

import sys
import getopt

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

#the n-gram value of n
gram = 0

#imput file 
inputfile = ""

#output file 
outputfile = ""

#smoothing technique
smoothTec = ""

#value of lambda for Lindston's smoothing
l_val = 1

#returns pts = list(option, value) and arg = the rest of the arguments
opts, args = getopt.getopt(sys.argv[1:], "n:i:o:s:", ["lmd="])

for opt, arg in opts:
    if opt == '-n':
        gram = arg
    elif opt == '-i':
        inputfile = arg
    elif opt == "-o":
        outputfile = arg
    elif opt == "-s":
        if arg not in ("wb", "ls"):
            print "invalid smoothing technique: " + arg
            sys.exit(2) 
        smoothTec = arg
    elif opt == "--lmd":
        l_val = arg

print "in file: " + inputfile
print "out file: " + outputfile
print "gram len: "  + gram
print "optional s: " + smoothTec