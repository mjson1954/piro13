count= int(input())
arr = []

for _ in range(count):
    number = int(input())
    if(number==0):
        arr.pop()
    else:
        arr.append(number)

print(sum(arr))