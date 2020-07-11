# string
ex_str="Hi I'm Minjoo, I'm a frontend developer"

# find, index
find_idx = ex_str.find("Minjoo")
index_idx = ex_str.index("Minjoo")
print(find_idx, index_idx)

find_none = ex_str.find("piro") # -1
# index_none = ex_str.index("piro") # error

try:
    index_none = ex_str.index("piro")
    print(index_none)
except Exception as e:
    index_none = -1
    print(e)

# split
splitted_list = ex_str.split(" ")
print(splitted_list)

# join
print(' '.join(splitted_list))
print('%20'.join(splitted_list))

# replace
replaced_str = ex_str.replace("Minjoo", "Piro")
print(replaced_str)

# strip
text = "      data data          "
print(text.strip()) # 공백은 없어지고 데이터만 나옴(안쪽의 공백은 없어지지 않음)
print(text.replace(" ","")) # 아예 공백 다 없애기

# f string (python 3.6 부터)
print(f'{text} 입니다') # format보다 이걸 권장

name = "손민주"
job= "프론트엔드"
print("안녕하세요. " + job + " 개발자 " + name + "입니다. ")
print("안녕하세요. {} 개발자 {}입니다.".format(job, name))
print("안녕하세요. {job} 개발자 {name}입니다.".format(job=job, name=name))
print(f'안녕하세요. {job} 개발자 {name}입니다.') # f string
introduction = f'안녕하세요. {job} 개발자 {name}입니다.' # 변수에 담을 수도 있음
print(introduction)

# list
# append, pop, del, remove

# extend
list1=[1,2,3]
list2=[4, 5]
list1.extend(list2)
print(list1) # 단점: 원본 리스트가 훼손됨

# dictionary
ex_dic = {
    "name": "Minjoo",
    "age" : 23,
    "job" :"developer",
}

ex_dic["address"] = "서울"
del(ex_dic["age"]) # 키를 이용해 삭제
print(ex_dic)

ex_keys = ex_dic.keys()
print(ex_keys) # 반환값이 리스트가 아님
ex_keys_list = list(ex_dic.keys())
print(ex_keys_list)

ex_value = list(ex_dic.values())
print(ex_value)


ex_items = list(ex_dic.items()) # 아이템을 튜플로 바꿔줌
print(ex_items)

# lambda

# 익명 함수 -> 함수인데 이름이 없다.
# 함수 호출 방법 -> 이름을 쓰고 인자를 준다.
# 사용 시기 : 간단한 함수 or 인라인에 사용할 때

# 람다 사용은 비추 -> 가독성이 떨어짐

print((lambda x, y: x + y)(1, 2)) # 첫번째 괄호가 람다 함수 선언부, 두번째 괄호가 인자 값
# 해석
def sum(x, y):
    return x + y 
print(sum(1, 2)) # 위의 람다 함수와 동일

# map -> list => func(item) => result_list
# map(function, list)
numbers = [1,2,3,4,5]
ex_map_1 = map(str, numbers)
print("map 1: ", ex_map_1)

ex_map_2 = list(map((lambda number: number + 10), numbers))
print("map 2: ", ex_map_2)

ex_map_3 = []
def sum10(number):
    return number+10

for number in numbers:
    result = sum10(number)
    ex_map_3.append(result)
print("map 3: ", ex_map_3)

# filter
ex_filter_1 = list(filter(lambda x: x > 3, numbers))
print(ex_filter_1)

def compare(x):
    return x>3

ex_filter_2=[]
for number in numbers:
    if compare(number):
        ex_filter_2.append(number)

print(ex_filter_2)