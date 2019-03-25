import sys

if (len(sys.argv) < 3):
	raise Warning("Pass input and output file names to script as command line arguments!")

try:
	inputFile = open(sys.argv[1], "r")
	outputFile = open(sys.argv[2], "w")
finally:
	outputFile.close()

def normalize(phone):
	replacements = (
		('-', ''),\
		('A', '2'), ('B', '2'), ('C', '2')\
		,('D', '3'), ('E', '3'), ('F', '3')\
		,('G', '4'), ('H', '4'), ('I', '4')\
		,('J', '5'), ('K', '5'), ('L', '5')\
		,('M', '6'), ('N', '6'), ('O', '6')\
		,('P', '7'), ('R', '6'), ('S', '7')\
		,('T', '8'), ('U', '8'), ('V', '8')\
		,('W', '9'), ('X', '9'), ('Y', '9')\
		)
	for repl in replacements:
		r1, r2 = repl
		phone = phone.replace(r1, r2)
	phone = phone[:3] + '-' + phone[3:]

	return phone
		


countOfDatasets = int(inputFile.readline()[:-1])

for phonessCounter in range(countOfDatasets):
	inputFile.readline()
	amountOfphones = int(inputFile.readline()[:-1]);
	phones = []

	for i in range(amountOfphones):
		phone = inputFile.readline()[:-1]
		phones.append(phone)

		normalized = []
	for phone in phones:
		normalized.append(normalize(phone))

	countedList = {x:normalized.count(x) for x in normalized if (normalized.count(x) > 1)}
	
	with open(sys.argv[2], "a") as outputFile:
		for phone in countedList:
			outputFile.write('{} {}\n'.format(phone, countedList[phone]))
