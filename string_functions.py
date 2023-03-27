def to_upper(sentence):
    result = []
    # if the character is small it ord value is between 97-122 inclusive
    # we substract 32 from the ord value to change to a small letter.
    for char in sentence:
        if 97 <= ord(char) <= 122:
            result.append(chr(ord(char) - 32))
        else:
            result.append(char)
    return "".join(result)

def to_lower(sentence):
    result = []
    # if character is capital there ord value is between 65-90 inclusive
    # we will add 32 to their ord value to change to capital leter
    # we will collect those and return by joining them
    for char in sentence:
        if 65 <= ord(char) <= 90:
            result.append(chr(ord(char) + 32))
        else:
            result.append(char)
    return "".join(result)

def capitalize(sentence):
    result = ""
    # if there is no character in sentence we will return empty 
    # other wise we will change the first characters to capital letter and change the 
    # remaining to small letter.
    if sentence:
        result += to_upper(sentence[0])
    result += to_lower(sentence[1:])
    return result