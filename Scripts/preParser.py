def preParser(name_file):
	doc = open(name_file, 'r') # Подключаем файл с проектом
	doc_text = doc.readlines() # Записываем его в переменную
	
	new_doc_text = ""
	for w in doc_text:
		for d in w:
			if d == "\n":
				new_doc_text += " "
			else:
				new_doc_text += d
	doc.close()

	f = open("new.html", "w")
	f.write(new_doc_text)
	f.close()
	
	return new_doc_text
