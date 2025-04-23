from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
# options = Options()
# options.add_argument('--headless')
# options.add_argument('--window-size=1920,1080')
driver = webdriver.Chrome()

url = f"https://www.audible.com/search"

driver.get(url)

#driver.maximize_window()

# pagination
pagination = driver.find_element(By.XPATH, '//ul[contains(@class, "pagingElements")]')
pagination_items = pagination.find_elements(By.XPATH, './/li')

last_page = int(pagination_items[-2].text)

# create lists to store the data
titles = []
authors = []
runtimes = []
prices = []
languages = []
releasedates = []
ratings = []
current_page = 1
while current_page <= last_page:
    container_div = driver.find_element(By.CLASS_NAME, 'adbl-impression-container')

    li_items = container_div.find_elements(By.XPATH, './/li[contains(@class, "productListItem")]')

  
    for li in li_items:

        # get the data elements
        title = li.find_element(By.XPATH, './/h3[contains(@class, "bc-heading")]')
        author = li.find_element(By.XPATH, './/li[contains(@class, "authorLabel")]')
        runtime = li.find_element(By.XPATH, './/li[contains(@class, "runtimeLabel")]')
        price = li.find_element(By.XPATH, './/p[contains(@class, " buybox-regular-price")]')
        language = li.find_element(By.XPATH, './/li[contains(@class, "languageLabel")]')
        releasedate = li.find_element(By.XPATH, './/li[contains(@class, "releaseDateLabel")]')
        rating = li.find_element(By.XPATH, './/li[contains(@class, "ratingsLabel")]')
        # add all the data to the lists
        titles.append(title.text)
        authors.append(author.text.split(':')[-1].strip())
        runtimes.append(runtime.text.split(':')[-1].strip())
        prices.append(price.text.split(':')[-1].strip())
        languages.append(language.text.split(':')[-1].strip())
        releasedates.append(releasedate.text.split(':')[-1].strip())
        ratings.append(rating.text.split('out of 5 stars')[0].strip())
    current_page += 1
    try:
        next_page = driver.find_element(By.XPATH, '//span[contains(@class, "nextButton")]')
        next_page.click()
    except:
        pass


driver.quit()

# create a dataframe
df = pd.DataFrame({
    'Title': titles,
    'Author': authors,
    'Runtime': runtimes,
    'Price': prices,
    'Language': languages,
    'Release Date': releasedates,
    'Rating': ratings
})

print(df.head())
# save the dataframe to a csv file
df.to_csv('audible_books.csv', index=False)
print("Data successfully saved to audible_books.csv")

