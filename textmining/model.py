from konlpy.tag import Okt
from nltk.tokenize import word_tokenize
import re

class SamsungReport:

    def __init__(self):
        pass

    @staticmethod
    def read_file():
        okt = Okt()
        okt.pos("삼성전자 글로벌센터 전자사업부", stem = True)
        filename = './data/kr-Report_2018.txt'
        with open(filename, 'r', encoding = 'utf-8') as f: # 안 하면 한글 깨짐. 'r'은 read의 뜻
            texts = f.read()
        return texts

    @staticmethod
    def extract_hangeul(texts):
        temp = texts.replace('\n', ' ') # 줄바꿈 띄어쓰기로 변환
        tokenizer = re.compile(r'[^ ㄱ-힣]') # 한글 있는 것만 뽑아내라
        temp = tokenizer.sub('', temp)
        return temp

    @staticmethod
    def chane_token(texts):
        tokens = word_tokenize()
        print(tokens[:7])