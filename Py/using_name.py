#!/usr/bin/python
# Filename: using_name.py

if __name__ == '__main__':
	print('This program is being run by itself'+ " " + __name__)
else:
	print('I am being imported from another module' + " " + __name__)