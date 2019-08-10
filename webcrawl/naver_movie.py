from bs4 import BeautifulSoup
from selenium import webdriver

class NaverMovie:

    def __init__(self, url):
        self.driver = webdriver.Chrome(executable_path = 'C:/Users/ezen/PycharmProjects/tensorflow190803/webcrawl/data/chromedriver')
        self.driver.get(url)
        self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')

    def scrap(self):
        html = self.soup.prettify()
        # print(html)
        all_divs = self.soup.find_all('div', attrs = {'class':'tit3'})
        print(all_divs)
        arr = [div.a.string for div in all_divs]
        for i in arr:
            print(i)
        self.driver.close()