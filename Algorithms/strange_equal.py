def is_strange_equal(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    letters = {} 
    values = set()
    for i in range(len(s)):
        if s[i] in letters:
            if letters[s[i]] != t[i]:
                return False
        else:
            if t[i] in values:
                return False
            letters[s[i]] = t[i]
            values.add(t[i])
    return True
print(is_strange_equal("agg", "xdd"))
print(is_strange_equal("mxyskaoghi", "qodfrgmslc"))
print(is_strange_equal("agg", "xda"))
