import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


url1 = "https://www.google.com"
def test_search_results():
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url1)
search_box = driver.find_element(By_XPATH,"//*[@id='tsf']/div[1]/div[1]/div[2]/div[1]/div/div[2]/input")
search_box.send_keys("iphone")
search_box.send_keys(Keys.RETURN)
search_results = driver.find_elements_by_Xpath("//*[@id='rso']")
assertlen(search_results) >= 10
driver.close()
