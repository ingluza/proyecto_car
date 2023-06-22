import scrapy
from scraper.items import CourseItem
from scrapy.crawler import CrawlerProcess


class CodigoFacilitoSpider(scrapy.Spider):
    name = "codigo_facilito"
    allowed_domains = ["codigofacilito.com"]
    start_urls = ["https://codigofacilito.com/cursos"]
    base_url = "https://codigofacilito.com"
    

    def parse(self, response):
        
        
        courses = ''
        for href in response.css("h2 a::attr(href)").extract():
            print(f"{self.base_url}{href}")
            yield scrapy.Request(f"{self.base_url}{href}", callback=self.parse_items)
        #pagination > div > a.next_page
        next_page = response.css('a.next_page::attr(href)').extract_first()
        print("-------------",next_page)
        if next_page:
            yield scrapy.Request(f"{self.base_url}{next_page}")
        
        # process = CrawlerProcess(settings={
        #     "FEEDS": {
        #         "out.json": {"format": "json"},
        #     },
        # })
        # process.crawl(CodigoFacilitoSpider)
        # process.start()

    
    def parse_items(self, response):
        course_item = CourseItem() 
        course_item['name'] = response.css('div.box header h1::text').get()
        course_item['description'] = response.css('div.box header div.f-top-small p::text').get()
        course_item['rating'] = response.css('div.box header div.f-top-16 div div p::text').get()
        yield course_item
        