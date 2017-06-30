#!/usr/bin/python
from sys import argv
import os

def listFiles(input_path):
	#os.walk generator to recursively list files and directory
	for root,dirs,files in os.walk(input_path,topdown=False): 
		for name in files:
			#combine path with file name
			print os.path.join(root, name)

if __name__ == "__main__":
	#list files from current or input directory path
	if len(argv) == 1:
		listFiles(".")
	else:
		listFiles(argv[1])