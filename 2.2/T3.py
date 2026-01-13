def is_palindrome(text):
    cleaned_text = ""
    for char in text:
        if char.isalnum():
            cleaned_text += char.lower()

    print("Cleaned text:", cleaned_text)  # DEBUG
    return cleaned_text == cleaned_text[::-1]


text = input("Enter text: ")
print(is_palindrome(text))