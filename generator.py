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
