def parser(doc_text):	
	f_1 = False; f_2 = False; f_3 = False; f_4 = False; f_5 = False; f_6 = False# Объявляем флаги
	i = 0; text = ""; teg = ""; c_teg = ""; space = {} # Объявляем вспомагательные переменные
	g = 0
	for w in doc_text:

		# Если во-второй раз встретили <, сообщаем об этом
		if w == "<" and f_1 == True: f_2 = True
		
		# Если наткнулись на знак начала тега запускаем запись
		if w == "<" and f_1 == False: f_1 = True  
		
		if f_3 == True: text += w
		
		# Если это не пробел, мы нашли второй тег и тег не найден
		if w != " " and f_2 == True and f_6 == False:
			c_teg += w

			if c_teg == "</p" and teg == "<p": f_6 = True
			if c_teg == "</img" and teg == "<img": f_6 = True
			if c_teg == "</table" and teg == "<table": f_6 = True

			if len(c_teg) > 7: f_2 = False; c_teg = ""

		# Если запись разрешена и тег не определён 
		if f_1 == True and f_3 == False: 
			if w in "<pimgtableh123456": # Добавляем только те символы из которыз состоят наши теги 
				teg += w
			if teg == "<p": f_3 = True; text += " "			
			if teg == "<img": f_3 = True; text += " "			
			if teg == "<table": f_3 = True; text += " "		

			if len(teg) > 6: teg = ""; f_1 = False

		# Если Нашли знак закрытия тега и тег закрытия найден кончаем
		if w == ">" and (f_6 == True or teg == "<img"):
			i+=1; space[i] = [teg + text, teg]
			f_1 = False; f_2 = False; f_3 = False; f_4 = False; f_5 = False; f_6 = False
			teg = ""; c_teg = ""; text = ""; g = 0;
		
		g += 1
		#print(g, " || ", w, " | ", text, " | ", teg, " | ", f_3, " | ", f_6 == True, " | ", c_teg )
	return space
