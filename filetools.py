#!/usr/bin/python3

"""
    Tools to manipulate corpus files. Written for my current linguistics
    research project.
    
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

CORPUS_PATH = './txts'
LIMIT = 'volume'

def comment_out_text_info(limit_word=LIMIT):
    """Comments out info which should not be taken into account
    by AntConc."""
    path_list = generate_path_list(CORPUS_PATH)
    for p in path_list:
        buff = []
        with open(p) as f:
            out = True
            for line in f:
                if not line.startswith('#'):
                    if line.lower().startswith(limit_word) and out:
                        out = False
                        buff.append('#' + line)
                    elif out:
                        buff.append('#' + line)
                    else:
                        buff.append(line)
        with open(p, 'w') as f:
            for i in buff:
                f.write(i)
                
def remove_sharp():
    path_list = generate_path_list(CORPUS_PATH)
    for p in path_list:
        buff = []
        with open(p) as f:
            for line in f:
                if not line.startswith('#'):
                    buff.append(line)
        with open(p, 'w') as f:
            for i in buff:
                f.write(i)

def generate_path_list(corpus_path):
    """Returns the paths of files of a corpus
    
    Returns the files in the form of a list of
    strings containing their paths.
    PLEASE NOTE THIS WILL ONLY WORK IN UNIX!"""
    
    path_list = []
    file_list = os.listdir(corpus_path)
    for f in file_list:
            path_list.append(os.path.join(corpus_path,f))
    return path_list

def check_double_titles(path_list):
    for p in path_list:
        with open(p) as f:
            l = f.readline()
            if l in title_list:
                print(l)
            else:
                title_list.append(l)
    for i in title_list:
        print(i)

def remove_figures():
    for p in generate_path_list('processed_txts'):
        running = True
        done = False
        while not done:
            done = True
            buff = []
            previous_line = 'none'
            out = False
            changed = False
            with open(p) as f:
                for line in f:
                    if line.lower().startswith(('figure', 'table', 'image')) or out:
                        out = True
                        os.system('clear')
                        print('Removal tool')
                        print('File: {}'.format(p))
                        print()
                        print(previous_line)
                        print(">>> " + line)
                        print()
                        cmd = input("Delete?(n/Y/q/r)").lower()
                        if cmd == 'q':
                            running = False
                            changed = False
                            done = True
                            break
                        elif cmd == 'r':
                            changed = False
                            done = False
                            break
                        elif cmd == 'n':
                            buff.append(line)
                            out = False
                            if line != '\n':
                                previous_line = line
                        else:
                            buff.append('')
                            changed = True
                            
                    else:
                        buff.append(line)
                        if line != '\n':
                            previous_line = line
            if changed:
                if input('Save file?(Y/n)') != 'n':
                    with open(p, 'w') as f:
                        for i in buff:
                            f.write(i)
        if not running:
            break

def main():
    remove_figures()



if __name__ == '__main__':
    main()
