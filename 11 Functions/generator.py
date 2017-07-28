#!/usr/bin/python3
# generator.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    try:
        for i in inclusive_range():
            print(i, end = ' ')
    except TypeError as e:
        print(e)
#----------------------------------------------------------------------
def inclusive_range(*args):
    """"""
    numargs=len(args)
    if numargs<1: raise TypeError('requires at least one argument')
    elif numargs==1:
        start=0
        step=1
        stop=args[0]
    elif numargs==2:
        (start,stop)=args
        step=1
    elif numargs==3:
        (start,stop,step)=args
    else: raise TypeError('inclusive_range expected at most 3 argument, got {}.'.format(numargs))
    i=start
    while i<=stop:
        yield i
        i+=step

if __name__ == "__main__": main()
