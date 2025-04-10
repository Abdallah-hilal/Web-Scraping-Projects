from itemadapter import ItemAdapter

class ScrapyProjectPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        # Function to clean and convert comma-separated numbers
        def clean_and_convert(value):
            if value:
                # Remove commas and convert to float or int
                value = value.replace(',', '')
                try:
                    # Try converting to float first
                    return float(value)
                except ValueError:
                    try:
                        # If it fails, try converting to int
                        return int(value)
                    except ValueError:
                        return value  # Return original if it cannot be converted
            return None

        # Convert 'population_2025' to int
        if 'population_2025' in adapter:
            adapter['population_2025'] = clean_and_convert(adapter['population_2025'])

        # Convert 'yearly_change' (percentage) to float
        if 'yearly_change' in adapter:
            if adapter['yearly_change'] and '−' in adapter['yearly_change']:
                adapter['yearly_change'] = (adapter['yearly_change'].replace('−', '-')) 

        # Convert 'density_per_km2' to float
        if 'density_per_km2' in adapter:
            adapter['density_per_km2'] = clean_and_convert(adapter['density_per_km2'])

        # Convert 'fertility_rate' to float
        if 'fertility_rate' in adapter:
            adapter['fertility_rate'] = clean_and_convert(adapter['fertility_rate'])

        # Convert 'land_area_km2' to float
        if 'land_area_km2' in adapter:
            adapter['land_area_km2'] = clean_and_convert(adapter['land_area_km2'])

        # Convert 'median_age' to float
        if 'median_age' in adapter:
            adapter['median_age'] = clean_and_convert(adapter['median_age'])

        # Convert 'migrants_net' to float (make sure to handle the minus sign correctly)
        if 'migrants_net' in adapter:
            if adapter['migrants_net'] and '−' in adapter['migrants_net']:
                adapter['migrants_net'] = (adapter['migrants_net'].replace('−', '-')) 
        

        # Convert 'net_change' to float
        if 'net_change' in adapter:
            if adapter['net_change'] and '−' in adapter['net_change']:
                adapter['net_change'] = (adapter['net_change'].replace('−', '-'))
            adapter['net_change'] = clean_and_convert(adapter['net_change'])

        # Convert 'urban_pop_percent' (percentage) to float
        if 'urban_pop_percent' in adapter:
            if adapter['urban_pop_percent'] ==  "" :
                adapter['urban_pop_percent'] = None  

        
        if 'world_share' in adapter:
            if adapter['urban_pop_percent'] ==  "" :
                adapter['urban_pop_percent'] = None  


        # Return the processed item
        return item



import mysql.connector

class SaveToMySQLPipeline:

    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='abdallah',  # your MySQL password
            database='population_data'  # make sure this DB exists
        )
        self.cur = self.conn.cursor()

        # Create table if it doesn't exist
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS countries (
                id INT NOT NULL AUTO_INCREMENT,
                country_or_dependency VARCHAR(255),
                population_2025 BIGINT,
                yearly_change VARCHAR(10),
                net_change BIGINT,
                density_per_km2 FLOAT,
                land_area_km2 FLOAT,
                migrants_net VARCHAR(50),
                fertility_rate FLOAT,
                median_age FLOAT,
                urban_pop_percent VARCHAR(10),
                world_share VARCHAR(10),
                PRIMARY KEY (id)
            )
        """)

    def process_item(self, item, spider):
        self.cur.execute("""
            INSERT INTO countries (
                country_or_dependency,
                population_2025,
                yearly_change,
                net_change,
                density_per_km2,
                land_area_km2,
                migrants_net,
                fertility_rate,
                median_age,
                urban_pop_percent,
                world_share
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            item.get("country_or_dependency"),
            item.get("population_2025"),
            item.get("yearly_change"),
            item.get("net_change"),
            item.get("density_per_km2"),
            item.get("land_area_km2"),
            item.get("migrants_net"),
            item.get("fertility_rate"),
            item.get("median_age"),
            item.get("urban_pop_percent"),
            item.get("world_share")
        ))
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()
