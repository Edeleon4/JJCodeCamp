
import time
#vars for example
listADemo = [1,2,3,4,5,6,7,8]
listBDemo = [6,7,8]
twoSum = 1

def slowTwoSum(listA,listB,x):
	print "slow twoSum"
	for elemA in listA:
		for elemB in listB:
			if elemA+elemB == x:
				return True
	return False

def fastTwoSum(listA,listB,x):
	print "fast twoSum"
	setA = {elem for elem in listA}

	for elemB in listB:
		if twoSum-elemB in setA:
			return True
	return False

# example of higher order function
def returnNamedSpeaker(name):
	return lambda text: name+ " said "+text

func = returnNamedSpeaker("Eddie")
print func("happy")

#time stamped function calls using higher order funcitons
# lambda is an equivalent to def func(params before :) return value after colon
def timeDifTwoSum(listA,listB,x,funcTwoSum):
	startTime = time.time()
	val = funcTwoSum(listA,listB,x)
	endTime = time.time()
	print "Elapsed time for func was : ",endTime-startTime
	return val

print timeDifTwoSum(listADemo,listBDemo,twoSum,slowTwoSum)
print timeDifTwoSum(listADemo,listBDemo,twoSum,fastTwoSum)
