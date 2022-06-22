from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import openpyxl

driver = webdriver.Chrome(executable_path='/Users/fergalflattery/Downloads/chromedriver')

path = "/Users/fergalflattery/OneDrive - Athlone Institute Of Technology/Applied Scripting Languages/Assignment/A00291231/nba2k20_players.csv"

workbook = openpyxl.load_workbook(path)