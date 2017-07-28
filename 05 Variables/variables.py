#!/usr/bin/python3
# variables.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    num = 42
    print(type(num),num)
    str = 'abc'
    print(type(str),str)    
    num = 42 / 9
    print(type(num),num)    
    num = 42//9
    print(type(num),num)  
    num = round(42 / 9)
    print(type(num),num)  
    num = round(42 / 9, 2)
    print(type(num),num)   
    num = 42%9
    print(type(num),num)  
    num = int(42.9)
    print(type(num),num)     
    num = float(42)
    print(type(num),num)  
    
    s="This is a string"
    print(s)
    
    s="This is a\nstring"
    print(s)
    
    s=r"This is a\nstring"
    print(s)      
    
    n = 42
    s="This is a {} string".format(n)
    print(s) 
    
    n = 42
    s="This is a %s string"%n
    print(s)
    
    s='''\
this is a string
line after line
of text and more
text.
'''
    print(s)    
    
    x=(1,2,3)
    print(type(x),x,x[2],x[1:3])
    
    y=[1,2,3]
    y.append(5)
    y.insert(0,0)
    print(type(y),y,y[2],y[1:3])
    
    x='string'
    print(type(x),x,x[2],x[1:3])
    
    x=(1,2,3,4,5)
    for i in x:
        print(i)
        
    x='String'
    for i in x:
        print(i)    
    
    d={'one':1,'two':2,'three':3,'four':4,'five':5}
    print(d)
    for k in d:
        print(k,d[k])
    
    for k in sorted(d.keys()):
        print(k,d[k])    
    for k in sorted(d.values()):
        print(k)    
    
    d=dict(
        one=1,two=2,three=3,four=4,five='five'
    )
     
    d['seven'] = 7
    print(d)
    for k in d:
        print(k,d[k])
    
    for k in sorted(d.keys()):
        print(k,d[k])    

if __name__ == "__main__": main()
