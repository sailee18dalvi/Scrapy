import scrapy
from scrapy.item import Item, Field


class ExampleItem(scrapy.Item):
    pass

class NewItem(scrapy.Item):
    # define the fields for your item here like:

    headline = Field()
    text = Field()
    url = Field()
    img = Field()

 
