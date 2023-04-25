def reading_time(text):
    if text == '':
        raise Exception ("You cannot input a blank string")
    if type(text) is not str:
        raise Exception ("input is not a string")
    word_count = len(text.split(" "))
    return word_count / 200

