# is Incomplete

import re
# a = {'beast', 'token', 'aster', 'tank'}
# regex1 = re.compile(r'^((?!as).)*$')
# filt_regex = [i for i in a if not regex1.search(i)]

wordLength = {
	2: {'to', 'as', 'be', 'aa'},
	3: {'alt', 'all', 'too', 'bee', 'too', 'ast'},
	4: {'salt', 'dart', 'blas', 'ally', 'bees', 'astr', 'aarp'}
}

global largestWord
global largestWordList

def loopFunc(wordList):
	for word in wordList:
		filterFunc(word)

def filterFunc(wordSearch):
	regex = '^((?!' + wordSearch + ').)*$'
	regex = re.compile(regex)

	if len(wordSearch)+1 in wordLength:
		filt_list = [i for i in wordLength[len(wordSearch)+1] if not regex.search(i)]
		if len(filt_list) > 0:
			print ('printing filt_list : ' + '\t'.join(filt_list))
			loopFunc(filt_list)
	print ('printing wordSearch : ' + wordSearch)
	print ('printing largestWord : ' + largestWord)
	if len(largestWord) < len(wordSearch):
		largestWord = wordSearch
		largeWordList = {}
		largeWordList.add(wordSearch)
		largestWordList = largeWordList

	if len(largestWord) == len(wordSearch):
		largestWordList.add(wordSearch)

loopFunc(wordLength[2])
print (largestWordList)
input('Press <Enter> to exit')