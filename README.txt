Open Concordance aims to be an easy to use concordance software and text and corpus analysis tool. It could be described as an Open Source alternative to Laurence Anthony's freeware concordance program Antconc (http://www.antlab.sci.waseda.ac.jp/software.html).

Requirements

Open Concordance is written in Python 3. If you do not already have it, you can download it for free at http://www.python.org/.

Running the program

The code is obviously at an early stage, so some things will have to be hardcoded by you if you wish to make it work. First, the folder containing your corpus should be in the same folder as the program. By default the program will look for a folder named "txts" and load all .txt files found in it. 
Please make sure your folder only contains .txt files.

Features

For now, the main part of the program, contained in corpus.py, allows you to:
-- Get basic corpus data: minimum text length (in tokens), maximum text length, average text --length
-- Perform a quick concordance to get the number of hits for a word
-- Produce a concordance output for a word, in a .txt file named {word}-concordance-results.txt found in the same directory the program is run from.

The other files are:
filetools.py: I used it for my own corpus research project, mostly formating.
generator.py: creates a corpus for testing purposes.
gui.py: a project for a gui written in Tkinter.