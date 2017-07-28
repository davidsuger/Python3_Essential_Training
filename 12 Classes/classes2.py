#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

########################################################################
class Animal:
    """"""
    #----------------------------------------------------------------------
    def talk(self):
        """"""
        print('I have something to say')

    #----------------------------------------------------------------------
    def walk(self):
        """"""
        print('I am walking')
        
    #----------------------------------------------------------------------
    def clothes(self):
        """"""
        print('I have nice clothes')

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        
class Duck(Animal):
    #----------------------------------------------------------------------
    def __init__(self,**kwargs):
        """"""
        self.variable=kwargs
        
    def quack(self):
        print('Quaaack!')

    def walk(self):
        super().walk()
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
    donald.quack()
    donald.walk()
    donald.clothes()

if __name__ == "__main__": main()
