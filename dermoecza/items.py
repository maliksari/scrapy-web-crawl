
from matplotlib import image
import scrapy


class DermoeczaItem(scrapy.Item):

    name = scrapy.Field()
    barcode = scrapy.Field()
    brand = scrapy.Field()
    image = scrapy.Field()
    url = scrapy.Field()
