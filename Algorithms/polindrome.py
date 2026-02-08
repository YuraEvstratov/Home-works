def its_palindrome(x: int) -> bool:
    if x < 0 or x % 10 == 0 and x != 0:
        return False    
    copy = x
    new_value = 0
    while x != 0:
        new_value = new_value * 10 + x % 10 
        x = x // 10
    return new_value == copy 


print(its_palindrome(1))
print(its_palindrome(121))
print(its_palindrome(123321))
print(its_palindrome(1234321))
print(its_palindrome(124321))
print(its_palindrome(2134321))