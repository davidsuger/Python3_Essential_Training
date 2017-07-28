#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Duck:
    #----------------------------------------------------------------------
    def __init__(self,**kwargs):
        """"""
        self.variable=kwargs
        
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    def set_color(self,color):
        self.variable['color']=color
        
    #----------------------------------------------------------------------
    def get_color(self):
        """"""
        return self.variable.get('color','black')
    #----------------------------------------------------------------------
    def set_variable(self,k,v):
        """"""
        self.variable[k]=v
    
    #----------------------------------------------------------------------
    def get_variable(self,k):
        """"""
        return self.variable.get(k,None)
        
        
def main():
    donald = Duck(feet=2)
    print(donald.get_color())
    print(donald.get_variable('color'))
    print(donald.get_variable('feet'))
    donald.walk()

if __name__ == "__main__": main()
