import pandas as pd # 검색한 것 중에서 특정한 값만 보기 위해서

class KrxCrawler:

    def __init__(self, url):
        self.url = url

    def scrap(self):
        code = pd.read_html("http://kind.krx.co.kr/disclosureSimpleSearch.do?method=disclosureSimpleSearchMain", header = '0')[0]
        print(code)