

def reading_from () :
	lst = open("entry.txt", "r").readlines() #its a list of list with file info
	lst2 = [] #list where the strings of lst will go in as lists
	count = 0 

	#splitting each line, which is a string into a list
	countr = 0
	for index in lst :
		lst2.append(lst[countr].split())
		countr += 1

	#removing spaces from the program
	for index in lst2 :
		countr = 0 #for tracking the position in a list of a list
		#print (type(lst2[countr]))
		for count in index :
			if (count == ' ') :
				#inserting comma at the empty space within a list of a list
				lst2[countr[count]].remove(" ") 
				countr += 1

	return lst2

def output (lstr2) :
	final = open("result.txt", "w")
	#need to convert each element, which is a list into a string
	#then convert the wholesome list into a string
	countr = 0

	
	for index in lstr2:
		#print (index)
		lstr2[countr] = ','.join(str(e) for e in index)
		final.write(lstr2[countr]) #writing one line
		final.write(",\n") #adding a comma to the last element + making new line
		countr += 1 

	final.close()
	return

output(reading_from())