import scrapy


class HousePrices(scrapy.Spider):
    name = 'thuephongtro'
    start_urls = [
        # f'https://thuephongtro.com/cho-thue-phong-tro-ha-noi?page={e}' for e in range(1, 160)
        'https://thuephongtro.com/cho-thue-phong-tro-ha-noi'
    ]

    def parse(self, response):
        # print(response.css('div#product-lists-web').get())
        for quote in response.css('.list-all-new div'):
            
            main_link = quote.css('.news-thumb a::attr("href")').get()
            if main_link is not None:
                yield response.follow(main_link, self.parse_main_page)

        # is_next = False
        # next_page = None
        # for page in response.css('.pagination a'):
        #     if is_next:
        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
        #         is_next = False
        #         next_page = None
        #     if 'actived' == page.css('::attr("class")').get():
        #         is_next = True

    
    def parse_main_page(self, response):
        description = ' '.join(response.css('.post_summary-content::text').extract())
        # location = ''
        # kind = ''
        location = kind = area = price = ''
        obj = {
            'Địa chỉ:': 'location',
            'Chuyên mục:': 'kind',
            'Diện tích:': 'area',
            'Giá cho thuê:': 'price'
        }
        main_obj = {
            'description': description
        }
        label = None
        for tr in response.css('.summary_row.clearfix div'):
            for td in tr.css('div'):
                txt = td.css('::text').get()
                if label is not None:
                    main_obj[obj[label]] = txt if label != 'Chuyên mục:' else td.css('a::text').get()
                    label = None
                if txt in obj.keys():
                    label = txt
        yield main_obj