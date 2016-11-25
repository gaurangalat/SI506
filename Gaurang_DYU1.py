import turtle								#import turtle library
name = raw_input ("May I know who is reading this? ")			#take in the name of the user

print "\n Hello", name,"I hope you like this little program"

print "\nThe main things I have learnt till date include - "

courselist = ["Variables and Values", "Simple Operations", "Boolean Expressions", "Logical Operators", "Debugging", "Turtle", "Strings and Operations", "Lists and Operations", "Iteration" ]						#list of entries
ƒ
for entry in courselist:						#for loop
    print "*",entry
    
print "\nI will be able to demonstrate only the first 6, the rest are already in use in this program"

demo= raw_input("\nWhat would you like to have a demo of? ")		#take input from user

if (demo=="Variables and Values"):					#for first entry
        a = raw_input ("\nEnter first number ")				#take inputs from user
        b = raw_input ("Enter second number ")
        c = a								#simple reassignment process
        a = b
        b = c
        print "Let's switch the values"
        print "The values of the two numbers are, respectively", a,b
        print "Interesting right?"
elif (demo=="Simple Operations"):					#for second entry
        a = raw_input("\nEnter larger number ")				#take inputs from user
        b = raw_input("Enter smaller number ")	
        a = int(a)							#type conversion
        b= int(b)
        print "a + b = ", a+b						#simple arithematic operations
        print "a - b = ", a-b
        print "a / b =", a/b
        print "a x b = ", a*b
	print "a ^ b = ", a**b
elif (demo == "Boolean Expressions"):   				#for third entry
        a = raw_input ("\nEnter first number ")
        b = raw_input ("Enter second number ")
        print "Are the numbers equal?",a==b				#example of Boolean expression
elif (demo=="Logical Operators"):					#for fourth entry
        a = raw_input ("\nEnter larger number ")
        b = raw_input ("Enter smaller number ")	
        print "Is first number larger?", a>b				#example of Logical operation
elif (demo=="Debugging"):						#for fifth entry
        print "\nIn this section, I learnt about the different types of error messages namely Name Error, Type Error, Syntax Error and their meaning"
elif (demo=="Turtle"):							#for sixth entry
        print "\nSorry you have no option but to watch this little turtle make its own shape"
        gau=turtle.Turtle()						#create turtle named gau
        window=turtle.Screen()
        turtle.pensize(5)						#set width 
        turtle.speed(0)							#set speed
        gau.forward(100)						#basic rurtle movement operations
        gau.left(90)
        gau.forward(100)
        gau.left(90)
        gau.forward(100)
        gau.left(90)
        gau.forward(100)
        gau.left(90)
        time.sleep(5)							#make the graphic window stay longer after completion
else:
        print "\n Are you sure? Please see the list and run again"	#just a condition to make the program a bit complete
    

