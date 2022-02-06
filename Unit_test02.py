import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url2 = "https://www.youtube.com/"
def test_youtube_search_results():
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url2)
search_box = driver.find_element_by_name("search_query")
search_box.send_keys("how to do testing")
search_box.send_keys(Keys.RETURN)
search_results = driver.find_elements_by_class_name("yt-lockup-video")
assertlen(search_results) >= 10,
driver.close()