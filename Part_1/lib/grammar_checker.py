def grammar_checker(string):
    special_chars = ["!",".","?"]
    if type(string) is not str:
        raise Exception("input must be a string!")
    
    if string == "":
        raise Exception("input cannot be a blank string!")
    
    if string[0].isupper() and any(char in special_chars for char in string[-1]):
        return "Your string starts with a capital letter and has correct punctuation at the end!"
    
    if string[0].isupper() and not any(char in special_chars for char in string[-1]):
        return "Your string starts with a capital letter but has incorrect punctuation at the end!"
    
    if not string[0].isupper() and any(char in special_chars for char in string[-1]):
        return "Your string does not start with a capital letter but has correct punctuation at the end!"
    
    if not string[0].isupper() and not any(char in special_chars for char in string[-1]):
        return "Your string does not start with a capital letter and has incorrect punctuation at the end!"
    

