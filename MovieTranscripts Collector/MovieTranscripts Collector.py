from bs4 import BeautifulSoup
import requests

root_url = "https://subslikescript.com/"


website_url = f"{root_url}movies_letter-A"
result = requests.get(website_url)


soup = BeautifulSoup(result.text, "lxml")

# pagination
pagination = soup.find("ul", class_="pagination")
pages = pagination.find_all("li", class_="page-item")
last_page = pages[-2].text

for page in range(1, int(last_page)+1):
    result = requests.get( f'{website_url}?page={page}')
    soup = BeautifulSoup(result.text, "lxml")
    



    box = soup.find("article", class_="main-article")

    links = box.find_all("a",href=True)

    links = [link['href'] for link in links]

    links = [f"https://subslikescript.com{link}" for link in links if link.startswith("/movie/") ]


    for link in links:
        try:
            result = requests.get(link)
            soup = BeautifulSoup(result.text, "lxml")
            box = soup.find("article", class_="main-article")
            title = box.find("h1").get_text()
            title = "".join(c for c in title if c.isalnum() or c in (' ', '-', '_')).strip()
            transcript = box.find("div", id="cue-app").get_text(strip=True, separator=" ")
        
        except Exception as e:
            print(f"----------------- Error: {e} link does not work: {link} ------------------------------")

        with open(f"{title}.txt", "w", encoding="utf-8") as file:
                file.write(transcript)


