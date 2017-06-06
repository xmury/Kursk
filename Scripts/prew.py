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