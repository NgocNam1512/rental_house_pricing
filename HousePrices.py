import scrapy


class HousePrices(scrapy.Spider):
    name = 'HousePrices'
    start_urls = [
        'https://batdongsan.com.vn/nha-dat-cho-thue-ha-noi/',
    ]

    def parse(self, response):
        for quote in response.css('div#product-lists-web'):
            
            main_link = quote.css('a.product-avatar::attr("href")').get()
            yield response.follow(main_link, self.parse_main_page)

        # next_page = response.css('li.next a::attr("href")').get()
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)
    
    def parse_main_page(self, response):
        title = response.css('#product-detail-web h1::text').get()
        print('title', title)
        price_css, area_css = response.css('.short-detail-wrap ul li span.sp2')
        yield {
            'price': price_css.css('span.sp2::text').get(),
            'area': area_css.css('span.sp2::text').get(),
            'title': title
        }