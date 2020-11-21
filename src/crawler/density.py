import scrapy


class HousePrices(scrapy.Spider):
    name = 'density'
    start_urls = [
        'https://www.citypopulation.de/en/vietnam/hanoi/admin/'
    ]

    def parse(self, response):
        # print(response.css('.content-items::text').extract())
        for quote in response.css('.rname'):
            # print(quote.css('::text').extract())
            name = quote.css('::attr("data-wiki")').get()
            area = quote.css('::attr("data-area")').get()
            density = quote.css('::attr("data-density")').get()
            # if main_link is not None:
            #     yield response.follow(main_link, self.parse_main_page)
            # print(main_link)
            yield {
                'name': name,
                'area': area,
                'density': density
            }
            

        # is_next = False
        # next_page = None
        # for page in response.css('.pagination a'):
        #     if is_next:
        #         next_page = page.css('::attr("href")').get()
        #         if next_page is not None:
        #             yield response.follow(next_page, self.parse)
        #         is_next = False
        #         next_page = None
        #     if 'actived' == page.css('::attr("class")').get():
        #         is_next = True

    
    def parse_main_page(self, response):
        main_obj = {
            'price': response.css('.price .value::text').get(),
            'area': response.css('.square .value::text').get(),
            'location': response.css('.address .value::text').get(),
            'description': response.css('.detail.text-content::text').get(),
            'date': response.css('.date::text').get()
        }

        location = kind = area = price = ''
        obj = {
            'Loại BDS': 'kind'
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