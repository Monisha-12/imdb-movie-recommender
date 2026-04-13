from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Chrome()
driver.get("https://www.imdb.com/search/title/?year=2024")

movies = []
storylines = []

time.sleep(3)

items = driver.find_elements(By.CLASS_NAME, "lister-item")

for item in items[:50]:  # limit for now
    try:
        name = item.find_element(By.TAG_NAME, "h3").text
        desc = item.find_element(By.CLASS_NAME, "text-muted").text
        
        movies.append(name)
        storylines.append(desc)
    except:
        continue

df = pd.DataFrame({
    "Movie Name": movies,
    "Storyline": storylines
})

df.to_csv("data/movies.csv", index=False)

driver.quit()