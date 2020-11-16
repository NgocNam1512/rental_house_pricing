import scrapy
import json


class HousePrices(scrapy.Spider):
    name = 'thuephongtro'
    start_urls = [
        # f'https://gateway.chotot.com/v1/public/ad-listing?region_v2=12000&cg=1050&limit=2000&o=40&st=u,h&page=1' for e in range(1, 259)
        f'https://gateway.chotot.com/v1/public/ad-listing?region_v2=12000&cg=1050&limit=50&o={50*i}&st=u,h&page={i+1}' for i in range(0, 103)
    ]

    def parse(self, response):
        # print(response.css('div#product-lists-web').get())
        
        data = response.css('::text').get()
        
        main_dict = json.loads(data)

        for e in main_dict['ads']:
            main_link = f'https://gateway.chotot.com/v1/public/ad-listing/{e["list_id"]}'
            yield response.follow(main_link, self.parse_main_page)
     

    
    def parse_main_page(self, response):
        yield json.loads(response.css('::text').get())