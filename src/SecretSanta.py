from Person import Person

def main(): 
	SecretSantaGroup = []
	with open("..\\resources\\people") as file:
		lines = file.readlines()
		for line in lines: 
			line = line.strip("\n")
			people = line.split("->")

			couple = []	

			for person in people: 
				person = person.strip().strip(")")
				NameEmail = person.split(" (")
				GiftGiver = Person(NameEmail[0], NameEmail[1])
				couple.append(GiftGiver)

			if (len(couple) > 1):
				couple[0].setPartner(couple[1])
				couple[1].setPartner(couple[0])

			SecretSantaGroup = SecretSantaGroup + couple
	for member in SecretSantaGroup:
		print "Name: " + member.getName()
		print "Email: " + member.getEmail()
		if (member.getPartner() is not None):
			print "Partner " + "Spencer Whyte" 
		print " "

if __name__ == "__main__":
	main()
