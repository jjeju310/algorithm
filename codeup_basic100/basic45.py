"""정수 3개를 입력받아 합과 평균을 출력해보자.
"""
a,b,c = map(int,(input().split()))
d = a+b+c
print(d)
print( format(d/3, ".2f") )