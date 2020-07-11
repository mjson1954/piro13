def check_group(word):
    last_alphabet =""
    alphabets = [] # 나온 alphabet list
    # aabb
    for letter in word:
        if letter == last_alphabet: # a
            continue
        else:
            if letter in alphabets:
                return False # 그룹 단어가 아님
            alphabets.append(letter) # [a, b]
            last_alphabet = letter # a->b update
    return True # for문을 모두 통과하면 그룹 단어

count = int(input()) # 단어 개수 입력받기
result=0 # 초기화

for _ in range(count):
    word = input() # 단어 입력받기
    if check_group(word):
        result+=1
print(result)
    
    #1. letter가 연속적인가? aabb-> 직전 알파벳이 letter와 같은지 체크
    #2. 이미 나왔던 단어인가? aabbaa 
    #3. 연속을 깨뜨린 letter가 이미 나왔던 단어인지 체크 -> False이면 그룹 단어가 아님