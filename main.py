from Scripts import parser as par
from Scripts import preParser as pre
from Scripts import generator as gen
from Scripts import style 
import os


def prework():
	i = 0; file = ""
	link = "libreoffice --convert-to html "
	# Удаляем все файлы в директории html
	os.chdir("./Documents/html")
	for w in os.listdir():
		os.remove(w)
	# и возвращаемся назад
	os.chdir("../docx")			#* Перейти в директорию с документом
	
	for w in  os.listdir(): 		#* Обнаружить документ .docx
		q = w[-5: len(w)]

		if q == ".docx" or ".doc" in q: 	
			i+=1; 	file = "doc_" + str(i) + ".html"
			
			os.rename(w, "doc_"+ str(i) + ".docx")	#	* Переименовать по форме
			os.system(link + "doc_"+ str(i) + ".docx")	# 	* Конвертировать в html
			os.system("mv " + file + " ../html")	#	* Переместить полученный документ в папку html
	os. chdir("../html")	
	return file

def cover_data(space, style):
	g = 0;
	f = open("data.html", "a")
	f.write(style)
	while g < len(space):
		g = int(g) + 1;
		text = str(g) + " --> " + str(space[g][0]) + "\n"
		f.write(text)
		f.write("\n")
	f.close() 	
	os.system("subl data.html")

file = prework()
#print("text = ",style.styleParser(pre.preParser(name_file)))
#(par.parser(pre.preParser(name_file)))
space = par.parser(pre.preParser(file))
#space = parser(name_file)
style = style.styleParser(pre.preParser(file))

cover_data(space, style)

gen.generator(space)
