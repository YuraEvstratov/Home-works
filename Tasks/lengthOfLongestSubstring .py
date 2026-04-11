def lengthOfLongestSubstring(s: str) -> int:
    max_len = 0
    left = 0
    values = set()
    for right in range(len(s)):
        while s[right] in values:
            values.remove(s[left])
            left += 1
        values.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring(" "))
print(lengthOfLongestSubstring("abcader"))