#!/usr/bin/python3

"""
    A tool to create a testing corpus for Open Concordance
    Copyright (C) 2014  Antoine Chesnais

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import os

def generate_test_corpus():
	if not os.path.exists("test_corpus"):
		os.mkdir("test_corpus")
	for i in range(20):
		with open('test_corpus/text_{}.txt'.format(str(i+1).zfill(2)), 'w') as f:
			f.write("Title\n")
			f.write("Random\nInformation at the beginning\n\n")
			f.write("INTRODUCTION\n")
			f.write("BLAh blah single research.\nLores ipsum dolores est.\n")
			f.write('Now the" figures will begin. To be or\n')
			f.write("Figure 1: some frame\n")
			f.write("blagureforfigs\n")
			f.write("figublag\n")
			f.write('not to be: that is the question!')
			f.write("\nMETHOD\n")
			for j in range(20):
				f.write("This is line {} of the text.\n".format(j+1))
			f.write("\nThe END!!!")
			
def main():
	generate_test_corpus()
	
if __name__ == '__main__':
	main()
