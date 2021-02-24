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

"""
#문자열 바꾸기(replace)
a="Life is too short"
print(a.replace("Life", "Your leg"))
#'Your leg is too short'
"""
"""
#문자열 나누기
a="a,b,c,d"
print(a.split(","))
#입력한 것 기준으로 나눠줌 ['a', 'b', 'c', 'd']
"""

#list-서랍장 처럼 변수 여러개를 묶는 역할
#ex 출석부
"""a = '이시영'
b = '박재용'
c = '이보라'

print(a)
print(b)
print(c)
"""
"""결과
이시영
박재용
이보라
"""

#->리스트로 바꾸면 아래와같이 함. 리스트안에 계속 리스트를 추가할 수 있음
"""a=['이시영','박재용','이보라',[1,2]]
print(a[3][1])
"""
#리스트 더하기
"""
a=[1,2,3]
b=[4,5,6]

#print(a+b)
print(a*3)
#결과 [1, 2, 3, 4, 5, 6]
#결과 [1, 2, 3, 1, 2, 3, 1, 2, 3]
"""
"""
#리스트 값 교체하기
a=['이시영','박재용','이보라']
a[0] = "이소라" #값 교체하기
print(a) 
"""

#연속되게 교체
"""
a=['이시영','박재용','이보라']
a[0:2] = ['이소라','이보소'] #값 교체하기
print(a) 
#결과 ['이소라', '이보소', '이보라']
"""
"""
#삭제
a=['이시영','박재용','이보라']
a[0:3] = [] #값 삭제하기
print(a)
#결과 []
"""
"""
#삭제2
a=['이시영','박재용','이보라']
del a[0:3] #값 삭제하기
print(a)
#결과 []
"""
"""
#추가한다 append 함수
a=['이시영','박재용','이보라']
a.append('이이이')
print(a)
#결과 ['이시영', '박재용', '이보라', '이이이']
"""
#정렬 sort 함수
"""
a=['이시영','박재용','이보라']
a.sort()
print(a)
#결과 ['박재용', '이보라', '이시영']  문제는 가나다, 알파벨, 숫자는 크기순
"""

#뒤집기 역순 Reverse()
"""
a=['이시영','박재용','이보라']
a.reverse()
print(a)
#결과 ['이보라', '박재용', '이시영']  
"""

#위치 반환(index)
"""
a=[1,5,3]
print(a.index(5))
"""

#insert 삽입 append는 뒤에 추가, insert는 특정 인덱스에 삽입가능
"""
a=[1,5,3]
a.insert(2,4)
print(a)
#결과 [1, 5, 4, 3]
"""
"""
#remove 값을 삭제해라
a=[1,5,3]
a.remove(1)
print(a)
#결과 [1, 5, 3]
"""

"""
#remove 값을 삭제해라. 값이 여러개있으면 가장앞에 1개만 지워짐
a=[1,5,3,1,1,1,1]
a.remove(1)
print(a)
#결과 [5, 3, 1, 1, 1, 1]
"""
"""
#pop 마지막 값을 제외
a=[1,5,3,]
a.pop()
print(a)
#결과 [1,5]
"""
"""
#count 리스트에 있는 x의 개수를 세준다
a=[1,5,3,]

print(a.count(1))
"""
#extend 리스트 확장

a=[1,5,3,]
a.extend([2,3])

print(a)
#결과 [1, 5, 3, 2, 3]




