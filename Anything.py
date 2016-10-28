def main(): 
	print "Enter your name"
	name = raw_input()
	HandleName(name)

def HandleName(name):
	if name == "Nadine":
		print "You rock!"
	elif name == "Aidan":
		print "I love you!"
	else:
		print "Welcome " + name + "! You must be new here"


if __name__ == "__main__":
	main()