from bs4 import BeautifulSoup
import time 
import pandas as pd
from selenium import webdriver
import requests

star_light= pd.read_csv("C:\Users\Manal\Desktop\project 128\bright_stars.csv")

remove= star_light.dropna()


df.radius*df.radius[0.102763]
df.mass*df.mass[0.000954588]

df.to_csv("clean.csv", index=True,index_label= "id")

merge_planet_df= pd.merge(bright_stars, clean.csv on = "id")

merge_planet_df = pd.to_csv("final_df_csv")