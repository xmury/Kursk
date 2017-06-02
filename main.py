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
		* Перейти в директорию с документом
		* Обнаружить документ .docx
		* Переименовать по форме
		* Конвертировать в html
		* Переместить полученный документ в папку html

	http://www.ilnurgi1.ru/docs/python/modules/os.html
'''


file = "test_1.html"

out_dir_file = "./Documents/html/"

link = "libreoffice --convert-to html "

os.chdir("./Documents/docx")
os.system(link + file)

#print("text = ",style.styleParser(pre.preParser(name_file)))
#(par.parser(pre.preParser(name_file)))
space = par.parser(pre.preParser(out_dir_file + file))
#space = parser(name_file)
style = style.styleParser(pre.preParser(out_dir_file + file))
'''
for w in range(1, len(space)+1):
	if space[w][1] == "<p":
		print(w, "> ", space[w][0])
'''
gen.generator(space)
