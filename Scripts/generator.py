def generator(space):
	i = 0; html = """
		<style>
   			.brd {
   			border: 4px double black; /* Параметры границы */
    		padding: 10px; /* Поля вокруг текста */
   			}
  		</style>
	"""	
	#print(html)
	while i < len(space):
		i+=1
		line = '<div class = "brd">' + space[i][0] + '</div>\n'   
		html += line
	doc = open("dinamic.html", "w")
	doc.write(html)
