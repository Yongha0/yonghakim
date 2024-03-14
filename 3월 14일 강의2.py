print("{0:d} {1:d}".format(1,2))
a, b = map(int,input("두 개의 정수를 입력해 주세요:").split())
if a&b == 0:
    print("{0:d}는(은) {1:d} 의 배수입니다.".format(a,b))
# 윤년 판별하기
year = int(input('연도를 입력하세요 : '))
is_leap_year = ((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0))
print(year, '년은 윤년입니까?', is_leap_year)

    
