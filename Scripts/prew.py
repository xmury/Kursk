import os
def prework():
	i = 0; file = ""
	link = "libreoffice --convert-to html "
	
	for w in  os.listdir(): 		#* Обнаружить документ .docx
		q = w[-5: len(w)]

		if q == ".docx" or ".doc" in q: 	
			i+=1; 	file = "doc_" + str(i) + ".html"
			
			os.rename(w, "doc_"+ str(i) + ".docx")	#	* Переименовать по форме
			os.system(link + "doc_"+ str(i) + ".docx")	# 	* Конвертировать в html
			os.system("mv " + file + "Doc/")	#	* Переместить полученный документ в папку html
	return file