#!/usr/bin/env python

a=11

for line in range(1,a):

    for table in range(1,line + 1):

        print (line * table, '\t', end="")

    print ("\n")
