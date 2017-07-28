#!/usr/bin/python3
# syntax.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    print("This is the syntax.py file.")
    a = 'one'
    print(type(a),a)
    b=7
    print(type(b),b)
    c,d=3,4
    print(c,d)
    e,f=5,'five'
    print(type(e),e,type(f),f)
    
    a,b=1,2
    s="Less than b" if a<b else "Not less than"
    print(s)
    
    print("a is less than b") if a<b else "a is not less than b"

if __name__ == "__main__": main()
