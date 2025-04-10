# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyProjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

   


class BookItem(scrapy.Item):
    country_or_dependency = scrapy.Field()
    population_2025 = scrapy.Field()
    yearly_change = scrapy.Field()
    net_change = scrapy.Field()
    density_per_km2 = scrapy.Field()
    land_area_km2 = scrapy.Field()
    migrants_net = scrapy.Field()
    fertility_rate = scrapy.Field()
    median_age = scrapy.Field()
    urban_pop_percent = scrapy.Field()
    world_share = scrapy.Field()





