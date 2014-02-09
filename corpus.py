import os, time, threading

class Corpus:
	def __init__(self, path=None):
		self.texts = {}
		if path and os.path.exists(path):
			if os.path.isdir(path):
				self.load_folder(path)
			else:
				self.load_text_file(path)

	def load_text_file(self, path):
		if not os.path.exists(path):
			raise IOError
		with open(path) as f:
			self.texts[path] = tokenize(f.read())

	def load_folder(self, path):
		print('Loading texts.')
		if not os.path.exists(path):
			raise IOError
		filelist = os.listdir(path)
		pathlist = []
		for f in filelist:
			pathlist.append(path+'/'+f)
		for p in pathlist:
			with open(p) as f:
				self.texts[p] = tokenize(f.read())
		print('Loaded {} texts.'.format(len(pathlist)))

	def get_token_size(self):
		size = 0
		for t in self.texts:
			size += len(self.texts[t])
		return size

	def concordance(self, word, left=10, right=10, case=False, output='std'):
		"""Aims to be your typical concordancer with KWIC.
		
		TODO: left_text and right_text made be made into lists to allow for easier 
		KWIC sorting.
		Also, max_right and max_left variables could be added to permit to oversee
		punctuation in span count, though apparently span count is done in characters,
		not words or tokens (as seen in AntConc)
		Obviously, implement search of multiple groups, and when that's functional, 
		regular expression search."""
		
		if case:
			match_func = lambda w, t: w == t
		else:
			word = word.lower()
			match_func = lambda w, t: w == t.lower() # word is already lowered, see line above
		results = []
		hits = 0
		for t in sorted(self.texts):
			for index, token in enumerate(self.texts[t]):
				if match_func(word, token):
					left_text = ""
					right_text = ""
					for i in range(max(0, index-left), index, 1):
						if self.texts[t][i].isalnum():
							left_text += ' ' + self.texts[t][i]
						elif self.texts[t][i] in ('.', '?', '!', ',', ';', ':', ')'):
							left_text += self.texts[t][i]
						else:
							left_text += ' ' + self.texts[t][i]
						
					for i in range(index + 1, min(index+right+1, len(self.texts[t])), 1):
						if self.texts[t][i].isalnum():
							right_text += ' ' + self.texts[t][i]
						elif self.texts[t][i] in ('.', '?', '!', ',', ';', ':', ')'):
							right_text += self.texts[t][i]
						else:
							right_text += " " + self.texts[t][i]
					results.append((token, left_text.strip(), right_text.strip(), t))
					hits += 1
		if output == 'txt':
			l_width = r_width = p_width = 0
			w_width = len(word)
			for r in results:
				l_width = max(l_width, len(r[1]))
				r_width = max(r_width, len(r[2]))
				p_width = max(p_width, len(r[3]))
				
			with open('{}_concordance_results.txt'.format(word), 'w') as f:
				f.write("There are {} hits.\n\n".format(hits))
				for r in results:
					f.write("{0:>{lw}} <{1:^{ww}}> {2:<{rw}}    in file {3:<{pw}}.\n\n".format(r[1], r[0], r[2], r[3], lw=l_width, rw=r_width, ww=w_width, pw=p_width))
		else:
			return hits, results
	
	def quick_concordance(self, word, case=False):
		if case:
			match_func = lambda w, t: w == t
		else:
			match_func = lambda w, t: w == t.lower() # word is already lowered, see two lines below
		hits = 0
		word = word.lower()
		for t in self.texts:
			for token in self.texts[t]:
				if match_func(word, token):
					hits += 1
		return hits
	
	def word_list(self, case=False, punc=False, num=False):
		for t in self.texts:
			pass
	
	def get_data(self):
		min_length = None
		max_length = None
		length_sum = 0
		for t in self.texts:
			length = len(self.texts[t])
			if min_length:
				min_length = min(length, min_length)
			else:
				min_length = length
			if max_length:
				max_length = max(length, max_length)
			else:
				max_length = length
			length_sum += length
		print("Smallest text is {} tokens long.".format(min_length))
		print("Longest text is {} tokens long.".format(max_length))
		print("Average length is {:2} tokens".format(length_sum/len(self.texts)))

def tokenize(string):
	tokens = []
	word = ''
	for char in string:
		if char.isalnum():
			word += char
		elif char not in (' ', '\n'):
			if word:
				tokens.append(word)
				word = ''
			tokens.append(char)
		else:
			if word:
				tokens.append(word)
				word = ''
	return tokens
	


def main():
	c = Corpus('txts')
	c.get_data()

if __name__ == '__main__':
	main()
