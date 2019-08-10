from textmining.model import SamsungReport

if __name__ == '__main__':
    sam = SamsungReport() # static이 아니라서 그럼
    sam.download()
    # print(sam.extract_noun())