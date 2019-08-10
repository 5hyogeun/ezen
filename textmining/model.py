from konlpy.tag import Okt
from nltk.tokenize import word_tokenize
import nltk
import re

class SamsungReport:

    def __init__(self):
        self.okt = Okt()

    def read_file(self):
        self.okt.pos("삼성전자 글로벌센터 전자사업부", stem = True)
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
    def change_token(texts):
        tokens = word_tokenize(texts)
        print(tokens[:7])
        return tokens

    def extract_noun(self):
        # 삼성전자의 스마트폰은 -> 삼성전자 스마트폰
        noun_tokens = []
        tokens = self.change_token(self.extract_hangeul(self.read_file()))
        for tokens in tokens:
            token_pos = self.okt.pos(tokens)
            temp = [txt_tag[0] for txt_tag in token_pos if txt_tag[1] == 'Noun']
            if len(''.join(temp)) > 1:
                noun_tokens.append("".join(temp))

        texts = " ".join(noun_tokens)
        print('------------추출된 명사 300 ------------')
        print(texts[:300])

    @staticmethod
    def download():
        nltk.download()