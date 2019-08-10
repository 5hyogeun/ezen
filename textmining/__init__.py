from textmining.model import SamsungReport

if __name__ == '__main__':
    # sam = SamsungReport() # static이 아니라서 그럼
    # sam.download()
    # print(sam.extract_noun())
    # sung = SamsungReport()
    # sung.read_stopword()

    txt = SamsungReport()
    txt.find_freq()