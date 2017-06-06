from Scripts import parser as par
from Scripts import preParser as pre
from Scripts import generator as gen
from Scripts import style, prew, cover 

file = prew.prework()
#print("text = ",style.styleParser(pre.preParser(name_file)))
#(par.parser(pre.preParser(name_file)))
space = par.parser(pre.preParser(file))
#space = parser(name_file)
style = style.styleParser(pre.preParser(file))

cover.cover_data(space, style)

gen.generator(space)
