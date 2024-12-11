def is_palindrome_possible(text):
    char_counts = {}
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    
    odd_count = 0
    for count in char_counts.values():
        if count % 2 != 0:
            odd_count += 1
    
    return odd_count <= 1, char_counts

def rearrange_to_palindrome(char_counts):
    half = []
    middle = ''
    
    for char, count in char_counts.items():
        if count % 2 == 0:
            half.extend([char] * (count // 2))
        else:
            half.extend([char] * (count // 2))
            middle = char
    
    return ''.join(half) + middle + ''.join(half[::-1])

def process_text(text):
    possible, char_counts = is_palindrome_possible(text)
    if possible:
        palindrome = rearrange_to_palindrome(char_counts)
        return f"Rearranged Palindrome: {palindrome}"
    else:
        return "It's not possible to rearrange the text into a palindrome."

# Input text
input_text = input("Enter the text: ")
result = process_text(input_text)
print(result)
