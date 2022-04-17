
def check_palindrome(text):
    if len(text) <= 1:
        return False
    text = text.strip().lower().replace(' ', '')
    return text == text[::-1]


if __name__ == "__main__":
    text = "Noon"
    print(check_palindrome(text))