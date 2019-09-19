def isAbecedarian(word):
    lastLetter = None
    for letter in word:
        if lastLetter != None:
            diff = ord(letter) - (lastLetter)
            if diff == 1 or diff == 0:
                lastLetter = letter
                continue
            else:
                return False
        else:
            lastLetter = letter
    return len(word) > 0

print(isAbecedarian("abcbcdef"))
            