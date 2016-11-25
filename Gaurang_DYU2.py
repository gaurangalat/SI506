#Week 2 Demonstrate your understanding

print "Do you want a demo of this week's DYU?\nA. Yes	B. Not again\n"		
inp = raw_input("Please enter your option: ")		#Take input from user
if (inp =="B" or inp =="b"):				
	print "Oh well nevermind"
elif(inp == "A" or inp =="a"):				#Check Option
 	print "\nHere are a few comic book characters"		
	d={"Batman" : "Robin", "Asterix": "Obelix", "Tintin" :"Snowy"}		#Dictionary Initialization
	print d.keys()								#Print keys of the dictionary
	x= raw_input("\nDo you want to know their sidekicks?\nA. Yes	B. No\n")
	if (x == "A" or x =="a"):						#Check for User Option
		y = raw_input("Which character's sidekick would you like to know about? ")	#Take input
		c=0
		for ele in d.keys():						
			if (y.upper()==ele.upper()):				#Compare input and key of ditcionary
				print d[ele], "is the sidekick of", y, "\n"	
			else:
				c+=1
			if(c==3):						#Invalid Input checker
				print "Please Check Again"					
	elif(inp =="B" or inp =="b"):						
		print "\nOh well nevermind"
	else:
		print "\nNevermind. Sorry to waste your time :)"
else:										#Invalid input checker
	print ("\nSorry, wrong option. Run again")
	
	
