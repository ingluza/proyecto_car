
from scrapy import Field, Item


class CourseItem(Item):

    name = Field()
    description = Field()
    rating = Field()
