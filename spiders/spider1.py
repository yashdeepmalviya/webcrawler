import scrapy
from ..items import QuotetutorialItem

class QuoteSpider(scrapy.Spider):

    name = 'netaporter'
    page_number = 2
    start_urls = [
        'https://www.net-a-porter.com/en-in/shop/clothing/tops?pageNumber=1'
    ]

    def parse(self,response):
        items = QuotetutorialItem()

        name = response.css('span.ProductItem24__designer::text').extract()
        price = response.css('.PriceWithSchema9__value span::text').extract()
        originalprice = response.css('.PriceWithSchema9__value span::text').extract()
        brand = response.css('.ProductItem24__name::text').extract()
        category = response.css('.FilterTags52__tag::text').extract()



        items['name'] = name
        items['price'] = price
        items['brand'] = brand
        items['originalprice'] = originalprice
        items['category'] = category

        yield items

    #next_page = response.css('div.Pagination7__nextCopy a::attr(href)').get()

    #if next_page is not None:
    #      yield response.follow(next_page, callback= self.parse)


        next_page = 'https://www.net-a-porter.com/en-in/shop/clothing/tops?pageNumber='+str(QuoteSpider.page_number)+'/'

        if QuoteSpider.page_number <= 25:
            QuoteSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
