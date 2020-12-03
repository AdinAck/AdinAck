#!/usr/bin/python
import json, sys

f = open(sys.argv[1], 'r'); x = json.load(f)

pathFile = open(sys.argv[2], 'r'); pathList = [line.rstrip('\n') for line in pathFile]

def do(x, pathList, prePath=""):
    for path in pathList:
        tmp = x; paths = path.split(".")
        for key in paths:
            doPrint = True
            if key == "*":
                if type(tmp) != type({}):
                    print("{}, {}".format(prePath, tmp))
                    doPrint = False; break
                else:
                    for key2 in tmp:
                        if len(paths[paths.index(key)+1:]) > 0: do(tmp[key2], paths[paths.index(key)+1:], prePath+".".join(paths[:paths.index(key)])+"."+str(key2))
                        else: print(prePath+".".join(paths[:paths.index(key)])+"."+str(key2))
                    doPrint = False; break
            else:
                try: tmp = tmp[key]
                except TypeError:
                    if type(tmp) == type([]):
                        print("Encountered list, printing contents of {}:".format(path))
                        doPrint = False
                        for i in tmp:
                            print(i)
                    else:
                        print("Encountered uniterable data type in", path)
                        doPrint = False
        if doPrint:
            if prePath != "": print("{}.{}, {}".format(prePath, path, tmp))
            else: print("{}, {}".format(path, tmp))

do(x,pathList)
