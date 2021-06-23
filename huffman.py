#!/usr/local/bin/python3
import sys
import argparse
import shutil
from collections import Counter

result='-'

class node:
    def __init__(self, freq, symbol, left=None, right=None):
        # frequency of symbol
        self.freq = freq
 
        # symbol name (charecter)
        self.symbol = symbol
 
        # node left of current node
        self.left = left
 
        # node right of current node
        self.right = right
 
        # tree direction (0/1)
        self.huff = ''
 
# utility function to print huffman
# codes for all symbols in the newly
# created Huffman tree
 
def save_char(symbol,result,fname,code):
	f = open(fname,'a')
	#print(result,end='')
	if code==False:
		f.write(result)
	else:
		f.write(result+':'+f'{symbol}'+'\n')
 
def printNodes(node, element,fname,code,val=''):
    # huffman code for current node
    newVal = val + str(node.huff)
 
    # if node is not an edge node
    # then traverse inside it
    if(node.left):
        printNodes(node.left, element,fname,code, newVal)
    if(node.right):
        printNodes(node.right,element,fname,code, newVal)
 
        # if node is edge node then
        # display its huffman code
    if(not node.left and not node.right and node.symbol == element):
        #print(f"{node.symbol} -> {newVal}")
    	result = newVal
    	save_char(node.symbol, result,fname,code)
        	

def encode(input_file, output_file):
	print("encoding ", input_file, output_file)
	# write code here
	inp_file = open(input_file,'r')
	out_file = open(output_file,'w+')
	out_file.write('')
	content = str(inp_file.read())
	count = dict(Counter(content))
	
	chars = list(count.keys())
	freq = list(count.values())

	# list containing unused nodes
	nodes = []
	 
	# converting ccharecters and frequencies
	# into huffman tree nodes
	for x in range(len(chars)):
	    nodes.append(node(freq[x], chars[x]))
	 
	while len(nodes) > 1:
	    # sort all the nodes in ascending order
	    # based on theri frequency
	    nodes = sorted(nodes, key=lambda x: x.freq)
	 
	    # pick 2 smallest nodes
	    left = nodes[0]
	    right = nodes[1]
	 
	    # assign directional value to these nodes
	    left.huff = 0
	    right.huff = 1
	 
	    # combine the 2 smallest nodes to create
	    # new node as their parent
	    newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)
	 
	    # remove the 2 nodes and add their
	    # parent as new node among others
	    nodes.remove(left)
	    nodes.remove(right)
	    nodes.append(newNode)
	 
	# Huffman Tree is ready!
	for char in content:
		printNodes(nodes[0],element=char,fname=output_file,code=False)

	print("Encoded..")

	f_code = open('code.txt','w+')

	for char in chars:
		printNodes(nodes[0],element=char,fname='code.txt',code=True)

	print("Codes stored..")


	# simply copying the file to bypass the actual test.
	# remove the below lines.
	#if input_file != "" and output_file != "":
	#	shutil.copyfile(input_file, output_file)


def decode(input_file, output_file):
	print("decoding ", input_file, output_file)
	# write code here

	f_code = open('code.txt','r')
	dic = {}
	codes = f_code.readlines()
	
	for code in codes:
		if ':' in code:
			temp = code.split(':')
			key = temp[0]

			if len(temp[1])==1:
				value = temp[1]
			else:
				value = temp[1].replace('\n','')

			dic[key] = value

	f_content = open(input_file,'r')
	f_decoded = open(output_file,'w+')

	content = f_content.readlines()
	output = ''
	
	code = ''
	for char in content[0]:
		code += char

		if code in dic.keys():
			output+=dic[code]
			code=''

	f_decoded.write(output)	

	print("Decod ended...")

	


	# simply copying the file to bypass the actual test.
	# remove the below lines.
	#if input_file != "" and output_file != "":
	#	shutil.copyfile(input_file, output_file)


def get_options(args=sys.argv[1:]):
	parser = argparse.ArgumentParser(description="Huffman compression.")
	groups = parser.add_mutually_exclusive_group(required=True)
	groups.add_argument("-e", type=str, help="Encode files")
	groups.add_argument("-d", type=str, help="Decode files")
	parser.add_argument("-o", type=str, help="Write encoded/decoded file", required=True)
	options = parser.parse_args()
	return options


if __name__ == "__main__":
	options = get_options()
	if options.e is not None:
		encode(options.e, options.o)
	if options.d is not None:
		decode(options.d, options.o)
