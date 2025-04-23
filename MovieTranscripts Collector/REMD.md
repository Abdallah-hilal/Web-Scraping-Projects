## 🎬 Movie Script Scraper — Subtitles from A to Z!

This project uses Python and BeautifulSoup to scrape **full movie transcripts** from [subslikescript.com](https://subslikescript.com), starting with titles that begin with the letter **A**. It collects script data across all paginated result pages and saves each movie’s script into a separate `.txt` file.

---

### 📄 What It Does

- 🔎 Navigates all pages of movies that start with **"A"**
- 🎥 Extracts each movie's:
  - Title  
  - Full script/transcript  
- 💾 Saves each script as a separate `.txt` file (named after the movie title)

---

### 🧰 Tech Stack

- Python  
- BeautifulSoup (bs4)  
- Requests  
- LXML (parser)

---

### 📁 Example Output

Each script is saved as a `.txt` file like:

```
The_Matrix.txt
Avengers_Endgame.txt
...
```

And contains:

> [Full transcript of the movie in plain text format]

---

### 💡 Why I Built It

I created this scraper to:
- Practice web scraping with **BeautifulSoup**  
- Build a dataset of movie scripts for **Natural Language Processing (NLP)** projects  
- Extract clean, ready-to-use text data for analysis or AI training

---

### ⚠️ Notes

- Skips broken links automatically with error handling  
- Cleans movie titles to create safe filenames  
- Only scrapes movies starting with the letter **A** (but can be extended to B-Z)

---

### 👨‍💻 My Contribution

I designed and implemented the entire scraper — from pagination and link extraction to downloading and saving script files.
