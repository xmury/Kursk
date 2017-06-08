import os

def cover_data(space, style):
	g = 0;
	f = open("data.html", "a")
	f.write(style)
	f.write("\n")
	while g < len(space):
		g = int(g) + 1;
		text = str(g) + " !!! " + str(space[g][0]) + "\n"
		f.write(text)
		f.write("\n")
	f.close() 	
	os.system("subl data.html")