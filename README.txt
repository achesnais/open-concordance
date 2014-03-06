Open Concordance aims to be an easy to use concordance software and text and corpus analysis tool. It could be described as an Open Source alternative to Laurence Anthony's freeware concordance program Antconc (http://www.antlab.sci.waseda.ac.jp/software.html).

Requirements

Open Concordance is written in Python 3. If you do not already have it, you can download it for free at http://www.python.org/.

Running the program

There are two ways to run the program:

If you have no knowledge of Python, you can use the gui (run gui.py) which is still under construction but works for basic, quick concordance (it will only give you hits). Simply use File > Open Directory to import your corpus (make sure that you are inside your corpus directory before clicking ok, not the directory containing it!). Then simply enter the word you are looking for and press the search button.

If you are not afraid to read some code and use the console, you can use corpus.py as a module. Simply supply the corpus path to the constructor's "path" argument.
Please make sure your corpus folder only contains .txt files, as the program will raise an exception (an error) if the folder contains anything it can't process. 

Features

For now, the main part of the program, contained in corpus.py, allows you to:
-- Get basic corpus data: minimum text length (in tokens), maximum text length, average text --length
-- Perform a quick concordance to get the number of hits for a word
-- Produce a readable concordance output for a word, in a .txt file named {word}-concordance-results.txt found in the same directory the program is run from.

The GUI only supports quick concordance (it will only return the number of hits).

The other files are:
filetools.py: I used it for my own corpus research project, mostly formating.
generator.py: creates a corpus for testing purposes.