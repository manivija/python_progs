def f(a):
    res = [a,1,a+1,0]
    return res[a%4]

def getXor(a, b):
     return f(b)^f(a-1)

cumulativeXor = 0
cumulativeXor_Eq = 0
length = 3
beginEntry = 0
for j in range(0, length):
    start = beginEntry + j * length
    end = beginEntry + j * length + length - (j + 1) + 1
    for entry in range(start,end):
        cumulativeXor ^= entry
    cumulativeXor_Eq ^= getXor(start, end - 1)
    #print(" ".join([str(x) for x in ( range (start, end) ) ]))
print ("\n" + str(cumulativeXor))
print ("\n" + str(cumulativeXor_Eq))
