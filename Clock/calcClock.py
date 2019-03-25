import sys

if (len(sys.argv) < 3):
	raise Warning("Pass input and output file names to script as command line arguments!")

try:
	inputFile = open(sys.argv[1], "r")
	outputFile = open(sys.argv[2], "w")
finally:
	outputFile.close()


def timeToAngle(h, m):
	if (h==12):
		h = 0

	angle = abs((60*h - 11*m) / 2)
	return angle
		

while True:
	rawTime = inputFile.readline()[:-1];
	time = rawTime.split(":")
	h, m = int(time[0]), int(time[1])

	if ((h == 0) and (m == 0)):
		break

	angle = timeToAngle(h, m)
	
	with open(sys.argv[2], "a") as outputFile:
		outputFile.write("{:.3f}\n".format(angle))
