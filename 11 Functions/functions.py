#!/usr/bin/python3
# functions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    testfunc(1,2,3,4)
    testfunc2(5,6,7,8,9,10,one=1,two=2,three=3)

def testfunc(x,y,*a):
    print('This is a test function',x,y)
    for n in a:
        print(n,end=' ')
#----------------------------------------------------------------------
def testfunc2(this,that,other,*args,**kwargs):
    """"""
    print()
    print(this,that,other)
    print(args)
    print(kwargs['one'])
    for k in kwargs:
        print(k, kwargs[k])
    

if __name__ == "__main__": main()
