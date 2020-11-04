import scrapy

class MainScpider(scrapy.Spider):
  name = 'main-spider'
  start_urls = ['https://educacao.uol.com.br/bancoderedacoes/propostas/carnaval-e-apropriacao-cultural.htm']

  def parse(self, response):
    # self.log('Eu estou aqui {}'.format(response.url))
    title = response.xpath('//i[@class="col-sm-22 col-md-22 col-lg-22 custom-title"]/text()').get()
    author = response.xpath('//p[@class="p-author-local"]/text()').get()
    texts =  response.css('p[style="margin-bottom:11px"]::text').extract()


    # texts = response.xpath('//span[@class="text"]/text()').extract()
    # for text in texts:
    #   yield {
    #     'text': text
    #   }
    
    
    yield {
      'title': title,
      'author': author,
      'texts': texts
    }
