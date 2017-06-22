from Scripts import parser as par
from Scripts import preParser as pre
from Scripts import generator as gen
from Scripts import style, prew, cover 
from Scripts import test

from bottle import get, post, request, run, route # or route
import os

def delit():
	ttt = os.listdir()
	for w in ttt:
		if ".html" in w or ".docx" in w:
			os.remove(w)
	ttt = os.listdir("Doc/")
	for w in ttt:
		os.remove("Doc/" + w)
@get('/') # or @route('/main')
def main():
	return '''
        <!DOCTYPE html>
		<html lang="en">
		<head>
			<meta charset="UTF-8">
			<title>Kurs</title>
		</head>
		<body align = center>
			<h1 align = center>Веб-сервис "Курс"</h1>
			<p align = center><b>Проверит характеристики вашего документа на соответствие ГОСТу принятому в ККАТ</b></p>			

	        <form action="/upload" method="post" enctype="multipart/form-data">
	  			Документ для проверки: <input type="file" name="upload" />
	  			<input type="submit" value="Отправить" />
			</form>
		</body>
		</html>
    '''

@route('/upload', method='POST')
def do_upload():
	delit()
	category   = request.forms.get('category')
	upload     = request.files.get('upload')
	name, ext = os.path.splitext(upload.filename)

	#save_path = get_save_path_for_category(category)
	upload.save("./") # appends upload.filename automatically


	file = prew.prework()
	#print("text = ",style.styleParser(pre.preParser(name_file)))
	#(par.parser(pre.preParser(name_file)))
	space = par.parser(pre.preParser(file))
	#space = parser(name_file)
	styl = style.styleParser(pre.preParser(file))

	cover.cover_data(space, styl)
	
	return test.start_test()
run(host="localhost", port=8001, debug=True)
