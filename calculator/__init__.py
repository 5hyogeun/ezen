from calculator.controller import CalculatorController

if __name__ == '__main__':
    num1 = int(input('첫 번째 수 : '))
    num2 = int(input('두 번째 수 : '))
    calc = CalculatorController(num1, num2)
    op = input('연산자 : ')
    result = calc.exec(op)
    print('계산결과 : %d' % result)