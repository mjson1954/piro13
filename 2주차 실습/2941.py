word_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

word = input()
for croatia in word_list:
    word = word.replace(croatia, "0")
print(len(word))