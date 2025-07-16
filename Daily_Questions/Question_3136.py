#Valid Word
class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        word = word.lower()
        vowel  = {'a','e','i','o','u'}
        v_n = 0
        c_n = 0
        for i in word:
            if not i.isalnum(): # a-z A-Z 0-9
                return False
            if i.isdigit(): # 0-9
                continue
            elif i in vowel:
                v_n += 1
            else:
                c_n += 1
        if v_n and c_n:
            return True
        else:
            return False