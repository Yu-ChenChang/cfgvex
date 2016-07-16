#!/usr/bin/python

start_var = 'a'

for i in range(10):
    firstline = "int wrapper_" + str(i) + "_args(int (*fc)("
    j = 0
    while j < i:
        if j < i - 1:
            firstline = firstline + "int, "
        else:
            firstline = firstline + "int"
        j = j+1
    firstline = firstline + ")"
    j = 0

    if i > 0:
        firstline = firstline + ", "

    while j < i:
        if j < i - 1:
            firstline = firstline + "int " + chr(ord(start_var) + j) + ", "
        else:
            firstline = firstline + "int " + chr(ord(start_var) + j)
        j = j+1
    firstline = firstline + ") {"
    secondline = "\tint ret = fc("
    j = 0
    while j < i:
        if j < i - 1:
            secondline = secondline + chr(ord(start_var) + j) + ", "
        else:
            secondline = secondline + chr(ord(start_var) + j)
        j = j + 1
    secondline = secondline + ");"
    thirdline = "\treturn ret;"
    fourthline = "}"

    print firstline
    print secondline
    print thirdline
    print fourthline
    print 
