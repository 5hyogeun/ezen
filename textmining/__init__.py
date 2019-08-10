from textmining.model import SamsungReport

if __name__ == '__main__':
    f = SamsungReport.read_file() # static 이면 바로 호출 가능
    print(SamsungReport.extract_hangeul(f))