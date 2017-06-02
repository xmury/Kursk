def generator(space, style):
	i = 0; html_1 = """
		
   			.brd {
   			border: 4px double black; /* Параметры границы */
    		padding: 10px; /* Поля вокруг текста */
   			}
  		</style>
	"""
	html = style[0:len(style)-8] + html_1
	
	print(html)
	#print(style)
	while i < len(space):
		i+=1
		line = '<div class = "brd">' + space[i][0] + '</div>\n'   
		html += line
	doc = open("dinamic.html", "w")
	doc.write(html)
