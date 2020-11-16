import scrapy


class HousePrices(scrapy.Spider):
    name = 'bds'
    start_urls = [
        'https://batdongsan.com.vn/nha-dat-cho-thue-ha-noi',
    ]

    def parse(self, response):
        # print(response.css('div#product-lists-web').get())
        for quote in response.css('div#product-lists-web div'):
            
            main_link = quote.css('a.product-avatar::attr("href")').get()
            if main_link is not None:
                yield response.follow(main_link, self.parse_main_page)

        is_next = False
        next_page = None
        for page in response.css('.pagination a'):
            if is_next:
                next_page = page.css('::attr("href")').get()
                if next_page is not None:
                    yield response.follow(next_page, self.parse)
                is_next = False
                next_page = None
            if 'actived' == page.css('::attr("class")').get():
                is_next = True

    
    def parse_main_page(self, response):
        title = response.css('#product-detail-web h1::text').get()
        description = response.css('.des-product::text').extract()
        price_css, area_css = response.css('.short-detail-wrap ul li span.sp2')[:2]
        location = ''
        kind = ''
        date = ''
        for e in response.css('.box-round-grey3 div.row-1'):
            if 'Địa chỉ:' in e.css('span.r1::text').get():
                location = e.css('span.r2::text').get()
            if 'Loại tin đăng:' in e.css('span.r1::text').get():
                kind = e.css('span.r2::text').get()
        label = None
        for e in response.css('.product-config.pad-16 ul li'):
            for s in e.css('span'):
                txt = s.css('::text').get()
                if label is not None:
                    date = txt
                    label = None
                if txt == 'Ngày đăng:':
                    label = txt
                
        yield {
            'price': price_css.css('span.sp2::text').get(),
            'area': area_css.css('span.sp2::text').get(),
            'title': title,
            'location': location,
            'type': kind,
            'description': description,
            'date': date
        }