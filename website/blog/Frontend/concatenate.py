
def function(b):
 	NMP =[int(x) for x in b.split()]
 	N = numpy.array([input().split() for i in range(NMP[0])], int)
 	M = numpy.array([input().split() for i in range(NMP[1])], int)
 	
 	return numpy.concatenate((N, M), axis = 0)

 __init__
print(function(input()))