import os



animalstable=[]

#This is to make the filepath relative to the script, rather than an absolute path or relative to the execution location
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'animals.dat')

if os.path.exists(filename) == False:
	filename = filename = os.path.join(dirname, 'start.dat')

#Open the animals.dat file
#Iterate over each line, stripping in to its components and storing it in an array
#This array is then used in the program, instead of manipulating the file, which is better and safer
with open(filename, 'r') as animalsfile:
	for line in animalsfile:
		row=[]
		for i in line.split('--'):
			row.append(i.lower().strip())
		animalstable.append(row)

#Then print the starting line	
print('Think of an animal. I will try to guess it.')

dummy=input('Press enter to start')


#The question index points to which question needs to be asked next. The first question is the zeroth questio
q_indx = 0
finished = False
#This loop will run forever until something breaks it
while True:
	#Ask the question
	answer = input(animalstable[q_indx][1]+' [y/n]:').lower()
	
	#Then select the appropriate action. For the answer we only look at the first letter, so that any form of yes will work.
	#2 is the column of the yes action, 3 is the column of the no action
	if answer[0].lower() == 'y':
		action = 2
	else:
		action = 3
	
	#If the action points to a new question(for this it must be a digit) then set the question index and repeat the loop.
	if animalstable[q_indx][action].isdigit():
		q_indx = int(animalstable[q_indx][action])
	else:
		#Else the program will try to guess the animal, and ask if its right. If yes, then succes! Otherwise, the program will run through a process to add the users animal and a appropriate
		#question to the database
		print('I think I know it !1!1')
		answer = input('Is it a {}? [y/n]:'.format(animalstable[q_indx][action]))
		if answer[0].lower() == 'y':
			print('epic!11!11!1one')
		else:
			print('frick')
			new_animal = input('What was the correct animal?:')
			new_q = input('Give yes/no question to distinguish {} from {}:'.format(new_animal, animalstable[q_indx][action]))
			new_answer = input('What is the anwer for {}? [y/n]:'.format(new_animal))
			
			#Add the new question to the database with the correct action order.
			if new_answer[0].lower() == 'y':
				animalstable.append([len(animalstable), new_q, new_animal, animalstable[q_indx][action]])
			else:
				animalstable.append([len(animalstable), new_q, animalstable[q_indx][action], new_animal])
	
			#Finally the question+action that pointed the program to the wrong guess is now pointed towards this new question
			animalstable[q_indx][action]=str(len(animalstable)-1)
			print('Your new entry has been added to the database')
		break
		

#Finally the new table/database needs to be written to the file. If a file is opened with 'w' then the contents of that file will be deleted. 
#Then the current table is written to the file.
with open('./animals.dat', 'w') as animalsfile:
	for row in animalstable:
		animalsfile.write('{} -- {} -- {} -- {}\n'.format(row[0],row[1].capitalize(),row[2],row[3]))
	
