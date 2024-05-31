def character_frequency(string):
    frequency = {}
    for char in string:
        if char.isalpha(): 
            char = char.lower()
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
    return frequency

if __name__ == "__main__":
    print(character_frequency("Hello World!")) 
    print(character_frequency("123 ABC abc!")) 
    print(character_frequency(""))  
    print(character_frequency("AaBbCc"))

