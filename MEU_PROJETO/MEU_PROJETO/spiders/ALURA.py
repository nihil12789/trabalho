import scrapy


class AluraSpider(scrapy.Spider):
    name = "ALURA"
    allowed_domains = ["www.alura.com.br"]
    start_urls = ["https://www.alura.com.br/cursos-online-programacao"]

    def parse(self, response):
        for curso in response.css('.subcategoria__item'):
            yield{
                'nome' : curso.css('.card-curso__nome ::text').get(),
                'link' : "https://www.alura.com.br" + curso.css('.card-curso ::attr(href)').get(),
                
                
            }
   
