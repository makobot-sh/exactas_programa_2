import scrapy
import html2text
import "funciones.py"

class MessiSpider(scrapy.Spider):
	name = 'messi'
	#allowed_domains = ['prueba.com']
	start_urls = ['https://pubmed.ncbi.nlm.nih.gov/?term=baldness&filter=simsearch2.ffrft&size=10']

	def parse(self, response):
		converter=html2text.HTML2Text()
		converter.ignore_links=True
		converter.ignore_images=True
		converter.ignore_tables=True
		text=converter.handle(response.css('*').get())
		text=text.encode('ascii','ignore')
		text=text.decode('utf-8')
		name = response.url.split('/')[2]
		f = open(name+".txt",'w')
		f.write(text)
		f.close()
		return text