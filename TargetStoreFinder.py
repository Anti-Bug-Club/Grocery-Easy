
# from multiprocessing.connection import wait
# from bs4 import BeautifulSoup
# from selenium import webdriver 
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait, Select
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())
# url='https://www.walmart.com/store/finder?location=91744&distance=50'
# driver.get(url)

# soup = BeautifulSoup(driver.page_source, 'html.parser')
# driver.quit()
# print(soup.prettify())

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
url='https://www.walmart.com/store/finder?location=91744&distance=50'
driver.get(url)
results =[]
content = driver.page_source

soup = BeautifulSoup(content)
driver.quit()
 
for a in soup.findAll(attrs= 'store-list'):
    name = a.find('li')
    if name not in results:
        results.append(name.text)
print(results)

df = pd.DataFrame({'Names' : results})
df.to_csv('names.csv', index=False, encoding='utf-8')

