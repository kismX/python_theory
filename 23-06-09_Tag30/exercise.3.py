# Write a function that checks whether a given string is a palindrome or not using a deque.
# Hint:
# use the popleft() und pop() methods

from collections import deque

def is_palindrome(word):
    word_deque = deque(word)

    if len(word_deque) <= 1:
        return True
    
    else:
        if word_deque[0] is word_deque[len(word_deque)-1]:
            word_deque.popleft()
            word_deque.pop()
            return is_palindrome(word_deque)
        else:
            return False
    


print(is_palindrome("radar"))   # True
print(is_palindrome("python"))  # False
print(is_palindrome("madam"))   # True