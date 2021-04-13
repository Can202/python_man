import getpass
import os

#Use man.pair(5), the result is False, it's not pair
def pair(num):
    result = True
    if num % 2 == 0:
        result = True
    else:
        result = False
    return result

#Use man.orderVector([0,2,3,20,5,2,50]), the result is order
def orderVector(vector):
	numberis = len(vector)
	torepeat = False
	repeathat = True

	while repeathat == True:
		i = 0
		for i in range(numberis):
			if i != 0:
				if vector[i] < vector[i-1]:
					torepeat = True
					m = vector[i-1]
					vector[i-1] = vector[i]
					vector[i] = m
		if torepeat == True:
			torepeat = False
			repeathat = True
		else:
			repeathat = False
	
	return vector

#Use man.reverseVector([0,2,5,1,5,34]), the result is reverse
def reverseVector(vector):
    numberis = len(vector)
    numberis2 = numberis // 2
    for i in range(numberis2):
        y = numberis - i - 1
        m = vector[i]
        vector[i] = vector[y]
        vector[y] = m
    return vector


#Use man.paused()
def paused():
    if os.name == "posix" or os.name == "mac":
        pause_var = getpass.getpass("Press Enter")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("pause")
    
    
#Use man.clear()
def clear():
    if os.name == "posix" or os.name == "mac":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")
