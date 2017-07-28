#!/usr/bin/python3
# files.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    inf = open('lines.txt')
    outf = open('new.txt','w')
    for line in inf:
        print(line, end = '',file=outf)

    buffersize=50000
    inf=open('bigfile.txt')
    outf=open('new2.txt','w')
    buffer = inf.read(buffersize)
    while len(buffer):
        outf.write(buffer)
        buffer = inf.read(buffersize)
        
if __name__ == "__main__": main()
