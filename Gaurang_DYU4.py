def DYU4(a=3,b=""):
	list1={"ls":"List files and folders of the directory", "cd":"Change directory", "cat":"Concatenate. Also used to list contents of file","grep":"Used to find required character/ word/ phrase in files"}
	if (a==1):
		print "Well nevermind!"
	elif(a==2):
		print b,":",list1[b]
	else:
		print "Check Options and run again"


print "Hello Jackie! Welcome to this week's DYU demo"
print "I have a list of the following Unix commands, which one do you want to know about? "
inp=raw_input("ls, cd, cat, grep\n")
x=int(raw_input("Do you want the demo? Enter 1 for NO, 2 for HEll YES! "))

DYU4(x,inp)

"""This is a simple program that shows the demo of passing parameters positionally to functions and alos lists some UNIX commands along with their functions.
THe function DYU4 has a dictionary with keys as the UNIX commands and the values as their function.
DYU4 accepts two parameters, one integer and one string. 
The values passed at the function unvocation are mapped onto the variables a,b in the function definition.
An if-else conditional block checks the user input and prints the function of the UNIX command. 