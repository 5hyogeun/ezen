from bs4 import BeautifulSoup
import urllib.request as url

class NaverKospi:

    def __init__(self, addr):
        self.addr = addr

    def scrap(self):
        html = url.urlopen(self.addr).read()
        soup = BeautifulSoup(html, 'html.parser')
        txt = soup.find(id = "KOSPI_now").text
        result = print("코스피 지수 : "+txt)
        return result