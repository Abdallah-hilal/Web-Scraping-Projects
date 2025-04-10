import scrapy
from scrapy_project.items import BookItem

class PopsiderSpider(scrapy.Spider):
    name = "popsider"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country/"]

    def parse(self, response):
        table_rows = response.css("table tr")  # Select all table rows
        for row in table_rows[1:]:
            book_item = BookItem()  # Create a new BookItem for each row

            # Extracting the data for each field using CSS selectors
            book_item['country_or_dependency'] = row.css('td a ::text').get()  # Country/Dependency
            book_item['population_2025'] = row.css('td::text').getall()[3].strip()  # Population 2025
            book_item['yearly_change'] = row.css('td::text').getall()[4].strip()  # Yearly Change
            book_item['net_change'] = row.css('td::text').getall()[5].strip()  # Net Change
            book_item['density_per_km2'] = row.css('td::text').getall()[6].strip()  # Density per Km^2
            book_item['land_area_km2'] = row.css('td::text').getall()[7].strip()  # Land Area Km^2
            book_item['migrants_net'] = row.css('td::text').getall()[8].strip()  # Migrants Net
            book_item['fertility_rate'] = row.css('td::text').getall()[9].strip()  # Fertility Rate
            book_item['median_age'] = row.css('td::text').getall()[10].strip()  # Median Age
            book_item['urban_pop_percent'] = row.css('td::text').getall()[11].strip()  # Urban Population Percentage
            book_item['world_share'] = row.css('td::text').getall()[12].strip()  # World Share

            yield book_item  # Yield the item for each row
