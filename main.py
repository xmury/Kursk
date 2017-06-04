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


file = prework()
#print("text = ",style.styleParser(pre.preParser(name_file)))
#(par.parser(pre.preParser(name_file)))
space = par.parser(pre.preParser(file))
#space = parser(name_file)
style = style.styleParser(pre.preParser(file))
'''
for w in range(1, len(space)+1):
	if space[w][1] == "<p":
		print(w, "> ", space[w][0])
'''
gen.generator(space)
