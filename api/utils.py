def is_palindrome(word: str) -> bool:
    return word == word[::-1]


def longest_palindrome(text: str) -> str:
    longest = ''
    text_size = len(text)
    for i in range(text_size):
        for j in range(0, i):
            chunk = text[j:i + 1]
            if is_palindrome(chunk):
                if len(chunk) > len(longest):
                    longest = chunk
    return longest
