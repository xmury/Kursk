f = open("./../Documents/html/data.html", "r")
data = f.readlines()

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
		if i == 2: i = 0; ttq += [tq]; tq = []
		if w == "}": f1 = False; i = 0; tq = []; data_style[dd] = ttq; ttq = []
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
	print(progon_2)
	for w in progon_2:
		kt = []; i = 0
		for d in progon_2[w]:
			i+=1
			if i == 2: i = 0; progon_2[w] = [kt]; kt = []
			else: kt += [d]; print(d)
	return progon_2


g=0; data_style = []; data_paragraph = {}
for w in data:
	g+=1
	if g == 1: data_style = test_style(w)
	if g > 1: data_paragraph[g] = [test_paragraph(w)]
	if g == 3: break

#print(data_style)
for w in data_paragraph:
	print(data_paragraph[w])
#print(data_paragraph[2])
