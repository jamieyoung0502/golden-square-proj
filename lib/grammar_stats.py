class GrammarStats:
    def __init__(self):
        self._true = 0
        self._false = 0

    def check(self, text):
        special_chars = ["!",".","?"]
        
    
        if text[0].isupper() and any(char in special_chars for char in text[-1]):
            self._true += 1
            return self._true
        else:
            self._false += 1
            return self._false


    def percentage_good(self):
        return int((self._true / (self._true + self._false)* 100))