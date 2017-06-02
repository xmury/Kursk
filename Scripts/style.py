def styleParser(name_file):
	
	f_1 = False; f_2 = False; f_3 = False; f_4 = False; f_5 = False; f_6 = False# Объявляем флаги
	i = 0; text = ""; teg = ""; c_teg = ""; space = {} # Объявляем вспомагательные переменные
	g = 0

	for w in name_file:
		if w == "<" and f_1 == False: f_2 = True
		
		if f_3 == True: text += w
		if w != " " and f_2 == True and f_3 == False:
			teg += w

			if teg == "<style": f_3 = True

			if len(teg) > 6: f_1 = False; teg = "" 

		if w == "<" and f_3 == True: f_4 = True

		if w != " " and f_4 == True and f_5 == False:
			c_teg += w

			if c_teg == "</style": f_5 = True

		if f_5 == True: text += ">";break
		
		g+=1
#		if g > 1400:
#			print(g, " || text = ", text, " | c_teg = ", c_teg)
#			input()
	return teg + text
