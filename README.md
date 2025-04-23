
#  Abdallah's Data Scraping Projects

Welcome to my collection of **Python-based web scraping projects**, where I explore real-world websites and extract valuable data using tools like **Selenium** , **BeautifulSoup** and **scrapy**. These projects helped me sharpen my skills in automation, data extraction, and cleaning — and they're all ready for further analysis or machine learning use!

## 🎧 1. Amazon Audible Audiobooks Scraper

Scrapes audiobook data from [Audible.com](https://www.audible.com/search), including book titles, authors, runtimes, prices, and more.

### 🔹 Features:
- Automatically navigates all pages
- Extracts:
  - 📚 Title
  - ✍️ Author
  - ⏱ Runtime
  - 💵 Price
  - 🌍 Language
  - 🗓 Release Date
  - ⭐ Rating
- Saves everything to `audible_books.csv`

### 🛠 Tech Used: `Python`, `Selenium`, `Pandas`  
### 📁 Output: `audible_books.csv`

---

## ⚽ 2. Football Match Results Scraper

Scrapes match results from [adamchoi.co.uk](https://www.adamchoi.co.uk/overs/detailed) for **12,500+ football matches** across all countries and leagues.

### 🔹 Features:
- Selects "All Matches"
- Loops through each country
- Collects:
  - 🗓 Match Date
  - 🏠 Home Team
  - ⚽ Score
  - 🛫 Away Team
  - 🌍 League/Country
- Saves all data to `matches.csv`

### 🛠 Tech Used: `Python`, `Selenium`, `Pandas`  
### 📁 Output: `matches.csv`

### 📌 Sample:
```csv
date_of_match,home_team,score,away_team,league
17-08-2024,Arsenal,2 - 0,Wolves,England
24-08-2024,Aston Villa,0 - 2,Arsenal,England
```

---

## 🎬 3. Movie Script Scraper — Subslikescript.com

Scrapes full movie transcripts from [subslikescript.com](https://subslikescript.com) for all movies starting with the letter **A** and saves them as `.txt` files.

### 🔹 Features:
- Loops through all paginated movie pages
- Extracts:
  - 🎞 Movie Title
  - 📜 Full Transcript
- Saves each transcript as a `.txt` file

### 🛠 Tech Used: `Python`, `BeautifulSoup`, `Requests`, `LXML`  
### 📁 Output: Individual `.txt` files like `Avengers_Endgame.txt`, `The_Matrix.txt`, etc.

---

## 🚀 What's Next?

I plan to:
- Use these datasets for **data visualization** and **machine learning projects**
- Explore more complex websites using **Splash or Scrapy**

