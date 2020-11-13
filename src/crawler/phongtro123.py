import scrapy


class HousePrices(scrapy.Spider):
    name = 'phongtro123'
    start_urls = [
        f'https://phongtro123.com/tinh-thanh/ha-noi?page={e}' for e in range(1, 209)
    ]

    def parse(self, response):
        # print(response.css('div#product-lists-web').get())
        for quote in response.css('.list-post li'):
            
            main_link = quote.css('a::attr("href")').get()
            if main_link is not None:
                yield response.follow(main_link, self.parse_main_page)

    
    def parse_main_page(self, response):
        description = ' '.join(response.css('#motachitiet p::text').extract())
        # location = ''
        # kind = ''
        location = kind = area = price = ''
        obj = {
            'Địa chỉ': 'location',
            'Loại tin rao:': 'kind',
            'Diện tích:': 'area',
            'Giá cho thuê:': 'price',
            'Ngày cập nhật:': 'date'
        }
        main_obj = {
            'description': description
        }
        label = None
        for tr in response.css('tr'):
            for td in tr.css('td'):
                txt = td.css('::text').get()
                if label is not None:
                    main_obj[obj[label]] = txt
                    label = None
                if txt in obj.keys():
                    label = txt
        yield main_obj