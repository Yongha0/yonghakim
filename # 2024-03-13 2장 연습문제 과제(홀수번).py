# 2024-03-13 2장 연습문제 과제(홀수번)

#연습문제 2.1
print(200, '+', 300, '+',400, '=', 200+300+400)

#연습문제 2.3
width = 30
height = 60
area = width * height
print(area)

#연습문제 2.5
밑변 = int(input('정사각형의 밑변을 입력하시오 : '))
area = 밑변**2
print('정사각형의 면적:',area)

#연습문제 2.7
print('10!=', 10*9*8*7*6*5*4*3*2)

#연습문제 2.9
print('섭씨','화씨')
for celcius in range(0,51,10):
    fahrenheit = (9/5) * celcius + 32
    print(celcius, fahrenheit)

#연습문제 2.11
fahrenheit = int(input('화씨온도를 입력하세요:'))
celcius = (fahrenheit-32)*5/9
print('화씨',fahrenheit,'도는 섭씨',celcius,'도 입니다.')

#연습문제 2.13
Pl = 3.141592
r = int(input('원의 반지름을 입력하세요 :'))
둘레 = 2*Pl*r
area = Pl*r**2
print('원의 둘레=',둘레, '원의 면적 =',area)

#연습문제 2.15
a = int(input('밑변을 입력하세요 : '))
b = int(input('높이를 입력하세요 : '))
c = (a**2 + b**2)**(1/2)
print('빗변 :', c)

#연습문제 2.17
print(2<<0, 2<<1, 2<<2, 2<<3, 2<<4, 2<<5, 2<<6, 2<<7, 2<<8, 2<<9)

#연습문제 2.19
정수 = int(input('정수를 입력하세요 :'))
답 = 정수 %2 == 0 and 0 <= 정수 <=100
print('입력된 정수는 0에서 100의 범위 안에 있는 짝수인가?',답)

#연습문제 2.21
정수 = int(input('정수를 입력하세요:'))

print('9의 2진수 값:', a)
print('9의 2진수 값에 대한 비트단위 부정값:',b)

#연습문제 2.23
정수 = int(input('세 자리 정수를 입력하세요;'))
a = 정수//100
b = (정수//10)%10
c= 정수%10
print('백의 자리 :',a)
print('십의 자리 :',b)
print('일의 자리 :',c)