def palindrome(str1):
    reverse_str=""
    for ch in str1:
        reverse_str=ch+reverse_str
    return str1==reverse_str
