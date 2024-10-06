
def count_vowels(word):
    vowels = 0
    for x in word:
        if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
            vowels += 1
        else:
            vowels += 0
    return vowels

# result = count_vowels("hooray")
# print(result)

