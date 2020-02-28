# Packages
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

class webScraping():
    # main block
    def getDataFromAmazon(self):
        driver = webdriver.Chrome("/home/akhila/web-scraping/chromedriver_linux64/chromedriver")
        driver.get("https://www.amazon.com/laptops")
        content = driver.page_source
        soup = BeautifulSoup(content,'html.parser')
        name = []
        price = []
        rating = []

        for data in soup.find_all('div',attrs={'class','s-item-container'}):
            itemName = data.find('h2',attrs={'class','a-size-base s-inline s-access-title a-text-normal'})
            itemPrice = data.find('span',attrs={'class','a-offscreen'})
            itemRating = data.find('span',attrs={'class','a-icon-alt'})
            self.checkItemType(itemName,name)
            self.checkItemType(itemPrice,price)
            self.checkItemType(itemRating,rating)
        print(len(name),len(price),len(rating))
        data = {'Product Name':name,'Product Price':price,'Product Rating':rating}
        df = pd.DataFrame.from_dict(data)
        df.to_csv('products.csv',index=False,encoding="utf-8")

    def checkItemType(self,item,arrayName):
        if type(item) != type(None):
            arrayName.append(item.text)
        else:
            arrayName.append('-')

# ws = webScraping
ws = webScraping()
ws.getDataFromAmazon()

    
