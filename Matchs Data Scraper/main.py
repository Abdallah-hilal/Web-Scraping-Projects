from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
from time import sleep

website_url = "https://www.adamchoi.co.uk/overs/detailed"
driver = webdriver.Chrome()
driver.get(website_url)

button = driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]')
button.click()

# Initialize empty lists to store all matches
all_dates = []
all_home_teams = []
all_scores = []
all_away_teams = []
all_leagues = []

# Get the country dropdown
dropdown = Select(driver.find_element(By.ID, "country"))

# Get all options from the dropdown
countries = [option.text for option in dropdown.options]

# Loop through each country
for country in countries:
    try:
        # Select the country
        dropdown.select_by_visible_text(country)
        league_dropdown = Select(driver.find_element(By.ID, "league"))
        league = league_dropdown.first_selected_option.text
        sleep(3)  # Wait for the page to load
        
        # Get all matches for this country
        matches = driver.find_elements(By.TAG_NAME, "tr")
        
        # Collect data for each match
        for match in matches:
            try:
                match_date = match.find_element(By.XPATH, './td[1]').text
                home = match.find_element(By.XPATH, './td[3]').text
                match_score = match.find_element(By.XPATH, './td[4]').text
                away = match.find_element(By.XPATH, './td[5]').text
                
                # Append data with the country/league name

                all_dates.append(match_date)
                all_home_teams.append(home)
                all_scores.append(match_score)
                all_away_teams.append(away)
                all_leagues.append(country)
            except:
                continue
    except:
        continue

# Create DataFrame with all matches
matches_df = pd.DataFrame({
    "date_of_match": all_dates,
    "home_team": all_home_teams,
    "score": all_scores,
    "away_team": all_away_teams,
    "league": all_leagues
})

matches_df.to_csv("matches.csv", index=False)
print(matches_df.head())
driver.quit()
