#!/usr/bin/env python3

import sys

"""
def bin2c(filename, arrayName):
    with open(filename, "rb") as f:
        data = f.read()
        
        sys.stdout.write("const unsigned int {:s}Size = {:d};\n".format(arrayName, f.tell()))

        sys.stdout.write("unsigned char {:s}[] = {{\n".format(arrayName))
        j = 0
        for i in data:
            sys.stdout.write("0x{:02x},".format(i))
            if j == 16:
                sys.stdout.write("\n")
                j = 0
            else: 
                j = j + 1
        if i != 0:
            sys.stdout.write("\n")    
        sys.stdout.write("};\n")


    return
"""

def readgb(filename):
    arr = []
    with open(filename, "rb") as f:
        data = f.read()
        
        for i in data:
            arr.append("{:02x}".format(i))


    return arr
    

def outFormat(array):
	for i, hex_value in enumerate(array):
            decimal_value = int(hex_value, 16)
            sys.stdout.write(f"rom_contents[{i}] = {decimal_value};")
            sys.stdout.write("\n") 

if __name__=='__main__':
    array = readgb(sys.argv[1])
    outFormat(array)
