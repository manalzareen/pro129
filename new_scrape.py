
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd



START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

# Webdriver
browser = webdriver.Chrome("chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

Scraped_data = []

def scrape_more_data(hyperlink):
    print(hyperlink)
    try:
        page= requests.get(hyperlink)
        soup= BeautifulSoup(page.contenet , "html.parser")
        temp_list=[]
         table_rows = bright_star_table.find_all("tr")

        for rows in table_rows:
        table_cols = row.find_all("td")
        data= row_data.text.strip()
        Scraped_data.append(temp_list)

        star_data=[]

        for  i in range(0,len(Scraped_data)):
        Star_name= Scraped_data[i][1]
        Distance= Scraped_data[i][3]
        Mass = Scraped_data[i][5]
        Radius= Scraped_data[i][6]
        lum= Scraped_data[i][7]
        required_data = [Star_names,Distance,Mass,Radius,lum]
        star_data.append(required_data)

headers = ["Star_name","Distance","Mass","Radius","lum"]

# Define pandas DataFrame   
star_dt_1 = pd.DataFrame(Star_data, columns=headers)

# Convert to CSV
star_df_1.to_csv("Scrape_Data.csv", index=True,index_label= "id")


