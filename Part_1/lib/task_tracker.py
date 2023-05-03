def task_tracker(text):
    if type(text) != str:
        raise Exception("Input type must be a string.")
    if text == "":
        raise Exception("This string must have some contents.")
    return "#TODO" in text.upper()
