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

#Use man.ordern([0,2,3,20,5,2,50]), the result is order
def ordern(array):
	numberis = len(array)
	torepeat = False
	repeathat = True

	while repeathat == True:
		i = 0
		for i in range(numberis):
			if i != 0:
				if array[i] < array[i-1]:
					torepeat = True
					m = array[i-1]
					array[i-1] = array[i]
					array[i] = m
		if torepeat == True:
			torepeat = False
			repeathat = True
		else:
			repeathat = False
	
	return array

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