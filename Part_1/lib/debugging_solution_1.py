def get_most_common_letter(text):
    counter = {}
    number = 0
    longest = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in text:
        if char.lower() in alphabet:
            counter[char] = counter.get(char, 0) + 1 
    for key in counter:
        if counter[key] > number:
            number = counter[key]
            longest.append(key)
        else:
            pass
    return longest
    

    


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")

