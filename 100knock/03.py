# -*- coding: utf-8 -*-

var = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
list = var.split(" ")
for ele in list:
	#print len(ele.replace(",","").replace(".",""))
	print len(ele.translate(None,",."))
