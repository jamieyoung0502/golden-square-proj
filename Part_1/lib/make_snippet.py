def make_snippet(string):
    words = string.split(" ")
    if len(words) <= 5:
        return string
    elif len(words) > 5:
        five_words = words[0:5]
        five_word_string = " ".join(five_words)
        return five_word_string + "..."