"""a = "I eat %d apples." % 3
print(a)"""

"""number = 10
day = 'three'
b = "I ate %d apples. so i was sick for %s days." %(number, day)
#$d = 정수, %f = 실수, %s = 문자열
print(b)
"""

"""c="I ate {ea} apples. so i was sick for {day} days.".format(day="5", ea="3")
#format이 뭔지?
print(c)
"""

"""name = "int"
a = f"나의 이름은 {name}입니다"
print(a)"""

"""
#소수점표현
a="%f" % 3.42134234
print(a)
#자릿수 짜르기
a="%0.4f" % 3.42134234
print(a)
"""

"""
#문자열 갯수세기
a = "hobby"
print(a.count('b'))
#a에서 b가 몇개있는지 개수 카운트
"""
"""
#문자열 갯수찾기
a = "hobby"
    #01234
print(a.find('b'))
#a에서 b가 몇번쨰에 있는지 없으면 -1이 나옴, 있으면 해당 문자의 index가 나옴
"""

"""
#join 쪼개기
a = ",".join("abcd")
#결과 a,b,c,d
print(a)
b = ",".join("a","b","c","d")
#결과 ["a","b","c","d"]
print(b)
"""
"""
#대문자 변환
a = "hi"
print(a.upper())

#소문자변환
b = "HI"
print(b.lower())

#공백제거
c = "          hi     "
print(c.strip())
"""
