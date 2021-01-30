import re

# 1. 从*.tex文件中找出来所有的引用，像这个样子\cite{zhao2017cvpr}，把引用的key都存下来.
def find_cites_from_tex(file_name):
	f = open(file_name)

    cite_keys = []
	for line in f:
		print line
		if line[0] == '%':
			continue
		else:
			all_cites = re.findall(r'\\cite\{[0-9a-zA-Z,_]*\}', line) # use the regex, return the found substr
			for cite in all_cites:
				offset = [6-1] # becaues the '{' is start at 6, we want to extract only keys.
				for m in re.finditer(',', cite):   # use the regex, return the position
					print '%d-%d: %s' %(m.start(), m.end(), m.group(0))
					offset.append(m.start())
				offset.append(len(cite)-1)
				for i in range(0, len(offset)-1):
					key = cite[offset[i]+1 : offset[i+1]]
					print key
					cite_keys.append(key)
	f.close()
    return cite_keys


# 2. 从*.bib文件中，找出所有cite_keys列表中的引用文献，并把其保存在一个新的*.bib文件中.
def extract_reference_from_bib(src_bib_filename, cite_keys, dst_bib_filename):
	f = open(src_bib_filename)

	
# test it
