"""
문제
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

TODO(string.lower(), upper()로 대소문자로 구분가능)
TODO(string.islower(), isupper()로 대소문자 여부 확인가능 모든 문자가 소문자, 대문자 일때만 True ex) temp = "TETE" 일때 temp.isupper()는 True)
TODO(dict에 접근할때 dict.get(value, 0)으로 기본값을 지정할 수 있음.)
"""

word = input().upper()
count_map = {}

for char in word:
    count_map[char] = count_map.get(char, 0) + 1

result = []
for char, count in count_map.items():
    if count == max(count_map.values()):
        result.append(char)

if len(result) > 1:
    print("?")
else:
    print(result[0])
