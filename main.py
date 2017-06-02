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
#import os
#os.system("libreoffice --convert-to html Дозиметр\ Курск.docx")
name_file = "Новыйдокумент.html"



#print("text = ",style.styleParser(pre.preParser(name_file)))
#(par.parser(pre.preParser(name_file)))
space = par.parser(pre.preParser(name_file))
#space = parser(name_file)
style = style.styleParser(pre.preParser(name_file))
'''
for w in range(1, len(space)+1):
	if space[w][1] == "<p":
		print(w, "> ", space[w][0])
'''
gen.generator(space, style)
