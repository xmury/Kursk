f = open("./../Documents/html/data.html", "r")
data = f.readlines()
f.close()
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
		kt = {}; i = 0; r = ""
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
			progon_1 += [teg_text]
			teg_text = ""
		if w == "{" or w == "}" or w == ">" or w == "<": progon_1 += w
	
	progon_2 = {}; body = []
	f1 = False; f2 = False; key = ""
	for w in progon_1:
 		if f2: body+=[w]; 
 		if f1: key = w; f1 = False; f2 = True
 	
 		if w == ">": f2 = False; progon_2[key] = body; body = []

 		if w == "<": f1 = True

	ty = []
	for w in progon_2:
		if w[0] == "/" or w == ">": ty += [w]
	
	for w in ty:
		del progon_2[w]	

	for w in progon_2:
		kt = []
		for d in progon_2[w]:
			if not (d == ">" or d == "style" or d == ''): kt += [d]
		progon_2[w] = kt
	for w in progon_2: 										# Получаем список ключей
		kt = {}; i = 0; r = ""; 
		for d in progon_2[w]:								# Получаем с
			i+=1
			if int(i) == 1: r = d
			if i == 2: i = 0; kt[r] = d; r = ""
		progon_2[w] = kt
	return progon_2

g=0; data_style = []; data_paragraph = {}
for w in data:
	g+=1
	if g == 1: data_style = test_style(w)
	if g > 1: data_paragraph[g] = [test_paragraph(w)]

def testing(data_paragraph, data_stylea):
	i=0; gost = {"line-height":"150%", "align":"justify", "text-indent":"0.49in", "face":"Times New Roman, serif", "font-size":"14pt"}
	f_1 = False; f_2 = False; f_3 = False; f_4 = False; 
	for w in data_paragraph: # Порядковый номер
		test = data_paragraph[w][0];  
		if "p" in test:
			if test['p']["align"] == gost["align"]: 
				f_1 = True
			else:
				# Добавляем в словарь
			if test['p']["line-height"] == gost["line-height"]:
				f_2 = True
			else:
				# 
			if test['p']["text-indent"] == gost["text-indent"]:
				f_3 = True
			else:

			if test['font']["font-size"] == gost["font-size"]:
				f_4 = True
			else:

		i+=1; print(i) 
			
		#print(test['p']["align"])
		#print(gost["align"])
		#if i==1:
		#	break
testing(data_paragraph, data_style)