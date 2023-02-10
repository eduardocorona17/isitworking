def modify_palindrome(s):
    if s == s[::-1]:
        for i in range(len(s)):
            for j in range(97, ord(s[i])):
                t = s[:i] + chr(j) + s[i+1:]
                if t < s and t == t[::-1]:
                    return t
    else:
        for i in range(len(s)):
            for j in range(97, 123):
                t = s[:i] + chr(j) + s[i+1:]
                if t < s and t == t[::-1]:
                    return t
    return ''
# print(modify_palindrome("aaabbbaaa"))

def modify_palindrome(s):
    if s == s[::-1]:
        t = [s[:i]+chr(j)+s[i+1:] for i in range(len(s)) for j in range(97, ord(s[i])) if s[:i]+chr(j)+s[i+1:] < s and s[:i]+chr(j)+s[i+1:] == (s[:i]+chr(j)+s[i+1:])[::-1]]
    else:
        t = [s[:i]+chr(j)+s[i+1:] for i in range(len(s)) for j in range(97, 123) if s[:i]+chr(j)+s[i+1:] < s and s[:i]+chr(j)+s[i+1:] == (s[:i]+chr(j)+s[i+1:])[::-1]]
    return min(t) if t else ''
print(modify_palindrome("oooyyyooo"))

def cardinalitySort(nums):
    return sorted(nums, key=lambda x: (bin(x).count("1"), x))
print(cardinalitySort(31))
