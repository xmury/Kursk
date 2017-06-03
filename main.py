'''
	Меж абзацный интервал = 1,5
	Шрифт = Times New Roman
	Кегль = 14
	выравнивание по ширине
	абзацный отступ в тексте = 1,25 см
'''
from Scripts import parser as par
from Scripts import preParser as pre
from Scripts import generator as gen
from Scripts import style 
import os

''' Алгоритм
		- Перейти в директорию с документом
		* Обнаружить документ .docx
		* Переименовать по форме
		* Конвертировать в html
		* Переместить полученный документ в папку html

	
'''
def prework():
	i = 0
	link = "libreoffice --convert-to html "
	os.chdir("./Documents/docx") 	#* Перейти в директорию с документом
	
	for w in  os.listdir(): 		#* Обнаружить документ .docx
		q = w[-5: len(w)]

		if q == ".docx" or ".doc" in q: 	
			i+=1; 	file = "doc_" + str(i) + ".html"
			
			os.rename(w, "doc_"+ str(i))	#	* Переименовать по форме
			os.system(link + "doc_"+ str(i))	# 	* Конвертировать в html
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
