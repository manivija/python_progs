# [F_ReverseLookup(i) for i in list(s)] == [F_ReverseLookup(i) for i in s]

def answer(s):

	def F_ReverseLookup(i):
		if i.islower():
			return chr(122 - ord(i) + 97)
		return i

	return ''.join([F_ReverseLookup(i) for i in s])

#STRING_IN = 'vmxibkgrlm'
STRING_IN = "Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"
print (answer(STRING_IN))