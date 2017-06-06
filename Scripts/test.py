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
	teg_text = ""; data_style = {}; h =[" ", ":", ";", "\n", "\t", "{", "}", ""]
	tt = []
	for w in teg:
		if w not in h:
			teg_text += w
		if w == " ":
			tt += [teg_text]
			teg_text = ""
		if w == "{" or w == "}": tt += w 
	return tt


g=0; data_style = []; data_paragraph = []
for w in data:
	g+=1;
	if g == 1: data_style = test_style(w)
	if g > 1: data_paragraph += [test_paragraph(w)]

#print(data_style)
print()
print(data_paragraph[0])