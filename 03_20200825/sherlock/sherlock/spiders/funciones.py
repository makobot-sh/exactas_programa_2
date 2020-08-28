def extraer_links(texto):
	i = 0
	texto.find('doi',i)
	while(index!=-1):
		substring = texto[index+5:index+32] #levanto el contendi


		i+=32
		index = texto.find('doi',i)