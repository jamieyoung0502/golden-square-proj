def count_words(string):
    words = string.split(" ")
    count = len(words)
    if count > 1:
        return f"This string has {count} words."
    elif string == "":
        return "You need to enter at least one word."
    elif count == 1:
        return f"This string has {count} word."
    