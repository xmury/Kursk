def test_style(teg):
	teg_text = ""; data_style = {}; h =[" ", ":", ";", "\n", "\t", "{", "}", ""]
	tt = []
	for w in teg:
		if w not in h:
			teg_text += w
		if w == " ":
			tt += [teg_text]
			teg_text = ""
		if w == "{" or w == "}": tt += w 
	
	dd = []; ww = 0; www = 0
	f1 = False
	i = 0; tq = []; ttq = []

	for w in tt:
		if w == "<style" or w == 'type="text/css">' or w == '': continue

		www = ww; ww = w
		if w == "{": f1 = True; dd = www
		if f1: 
			i+=1; 
			if w == "{" or w == "}":
				pass
			else: tq += [w]
		if i == 2: i = 0; ttq += tq; tq = []
		if w == "}": f1 = False; i = 0; tq = []; data_style[dd] = ttq; ttq = []
	
	for w in data_style:
		kt = {}; i = 0; r = "";
		for d in data_style[w]:
			i+=1; 
			if int(i) == 1: r = d
			if i == 2: 
				kt[r] = d; i = 0
		data_style[w] = kt

	return data_style

def test_paragraph(teg):
	nur = []
	teg_text = ""; data_style = {}; h =[" ", ":", ";", "\n", "\t", "{", "}", "", "=", "\'", "\"", "<", ">"]
	progon_1 = []
	for w in teg:
		if w not in h:
			teg_text += w
		if w == " " or w == ">" or w == "<" or w == "=":
			progon_1 += [teg_text]; 
			teg_text = ""
		if w == "{" or w == "}" or w == ">" or w == "<": progon_1 += w
	
	progon_2 = {}; body = []
	f1 = False; f2 = False; key = ""
	for w in progon_1:
		if f2: body+=[w]; 
		if f1: key = w; f1 = False; f2 = True
		
		if w == ">": 
			f2 = False; 
			if key in progon_2:
				qw = progon_2[key]
				progon_2[key] = qw + body;
			else:
				progon_2[key] = body; body = []; 

		if w == "<": f1 = True

	ty = []
	# Находим мусорные элементы и удаляем	
	for w in progon_2:
		if w[0] == "/" or w == ">": ty += [w]
	for w in ty:
		del progon_2[w]	
	# Находим мусорные элементы и удаляем

	for w in progon_2:
		kt = []
		for d in progon_2[w]:
			if not (d == ">" or d == "style" or d == ''): kt += [d]; 
		progon_2[w] = kt; 

	for w in progon_2: 										# Получаем список ключей
		kt = {}; i = 0; r = ""; gg = False; ttt = "" 
		for d in progon_2[w]:								# Получаем с
			if d == "size": gg = False; kt["face"] = ttt; ttt = ""
			if gg: ttt += d + " "
			if d == "face": gg = True
			if gg == False:
				i+=1;
				if int(i) == 1: r = d
				if i == 2: i = 0; kt[r] = d; r = ""
		progon_2[w] = kt;
	return progon_2

def testing(data_paragraph, data_stylea):
	i=0; gost = {"line-height":"150%", "align":"justify", "text-indent":"0.49in", "face":"Times New Roman, serif ", "font-size":"14pt"}
 
	dic = {}
	for w in data_paragraph: # Порядковый номер
		d1 = True; d2 = True
		f_1 = False; f_2 = False; f_3 = False; f_4 = False; f_5 = False
		test = data_paragraph[w][0];  
		# Проверяем на соответствие ГОСТу
		if "p" in test:
			if test['p']["align"] == gost["align"]: 
				f_1 = True
			if test['p']["line-height"] == gost["line-height"]:
				f_2 = True
			if test['p']["text-indent"] == gost["text-indent"]:
				f_3 = True
		else:
			d1 = False
		if "font" in test:
			if "font-size" in test['font']:
				if test['font']["font-size"] == gost["font-size"]:
					f_4 = True
			if "face" in test['font']:
				if test["font"]["face"] == gost["face"]:
					f_5 = True
				else: print(test["font"]["face"], " <--|--> ", gost["face"])
		else: 
			d2 = False
		# Проверяем на соответствие ГОСТу

		# Добавляем в словарь теги с кривыми настройками
		error = " По ГОСТу должно быть: "
		if d1 and d2:	
			if f_1 == False:
				error += "выравнивание по ширине"
			if f_2 == False:
				if f_1 == False: error += ", межстрочный интервал 1.5"
				else: error += "межстрочный интервал 1.5"
			if f_3 == False:
				if f_1 == False and f_2 == False: error += ", отступ первой строки 1,25см"
				else: error += "отступ первой строки 1,25см"
			if f_4 == False:
				if f_1 == False and f_2 == False and f_3 == False: error += ", кегль 14pt"
				else: error += "кегль 14pt"
			if f_5 == False:
				if f_1 == False and f_2 == False and f_3 == False and f_4 == False: error += ", шрифт Times New Roman, serif"
				else: error += "шрифт Times New Roman, serif"
			if f_1 and f_2 and f_3 and f_4 and f_5:
				pass
			else: dic[w] = {"body":test, "error":error}
		# Добавляем в словарь теги с кривыми настройками
	return dic

def start_test():
	# Считываем входные данные
	f = open("./../Documents/html/data.html", "r")
	data = f.readlines()
	f.close()
	# Считываем входные данные
	
	# Извлекаем настройки
	g=0; data_style = []; data_paragraph = {}
	
	for w in data:
		g+=1
		if g == 1: data_style = test_style(w)
		if g > 1: data_paragraph[g] = [test_paragraph(w)]
	# Извлекаем настройки

	# Сверяем с ГОСТом
	dic = testing(data_paragraph, data_style)
	# Сверяем с ГОСТом
	for w in dic:
		print(w, " |\n", dic[w]["error"])
	# Возвращаем 
	return dic
a = start_test()