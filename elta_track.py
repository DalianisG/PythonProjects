# We need to scaffold a new scrapy project and create a new spider first
import scrapy


class EltaTrackSpider(scrapy.Spider):
    name = 'elta_track'
    allowed_domains = ['itemsearch.elta.gr/el-GR/Query/Direct/WT354988719GR']
    start_urls = ['https://itemsearch.elta.gr/el-GR/Query/Direct/WT354988719GR']

    def parse(self, response):
        for product in response.xpath("//div[@class='col col-md-10']/div/table/tbody/tr"):
            yield {
                'Date': product.xpath(".//td/text()").get(),
                'Situation': product.xpath(".//td/text()").get(),
                'Region': product.xpath(".//td/text()").get()
            }


#Using command "scrapy crawl elta_track -o data.csv" we can extract our data to a csv file


