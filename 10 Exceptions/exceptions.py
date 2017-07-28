#!/usr/bin/python3
# exceptions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC

def main():
    try:
        fh = open('xlines.txt')
        for line in fh: print(line.strip())
    except IOError as e:
        print('could not open the file:', e)
    
    run()

#----------------------------------------------------------------------
def readfile(filename):
    """"""
    if filename.endswith('.txt'):
        fh=open(filename)   
        return fh.readlines()
    else:
        raise ValueError('Filename must end with .txt')

#----------------------------------------------------------------------
def run():
    """""" 
    try:
        for line in readfile('xlines.trxt'):
            print(line.strip())
    except ValueError as e:
        print('bad file: ',e)
    except IOError as e:
        print('could not open the file:', e)
        
if __name__ == "__main__": main()
