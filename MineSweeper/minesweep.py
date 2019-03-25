import sys

if (len(sys.argv) < 3):
	raise Warning("Pass input and output file names to script as command line arguments!")

try:
	inputFile = open(sys.argv[1], "r")
	outputFile = open(sys.argv[2], "w")
finally:
	outputFile.close()

def inc(arr, i, j):
	chars = [(i-1, j-1), (i-1, j), (i-1, j+1),  (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]
	for char in chars:
		x, y = char
		if (arr[x][y] != '*'):
			arr[x][y] += 1


numberOfField= 0
while True:
	sizeOfField = inputFile.readline()[:-1].split(' ')	# remove new line caracter and split into two numbers		

	try:
		n, m = int(sizeOfField[0]), int(sizeOfField[1])
	except ValueError: # for case we havent emty line in end of file
		break

	if (n + n == 0):
		break

	numberOfField+= 1
	field = []
	field.append([0 for i in range(0, m + 2)]) # additional first empty line
	for i in range(0, n):
		line = inputFile.readline()[:-1]
		row = [('*' if (line[i] == '*') else 0) for i in range(0, m)] 
		field.append([0] + list(row) + [0])	# line of '*' and 0 followed and preceded by 0
	field.append([0 for i in range(0, m + 2)]) # additional last empty line

	for i in range(1, n+1):
		for j in range(1, m+1):
			if field[i][j] == '*':
				inc(field, i, j)

	with open(sys.argv[2], "a") as outputFile:
		outputFile.write('Field #' + str(numberOfField) + '\n')
		for row in field[1:-1]:
			outputFile.write(''.join(str(el) for el in row)[1:-1] + '\n')
