def to_upper(sentence):
    result = []
    for char in sentence:
        if 97 <= ord(char) <= 122:
            result.append(chr(ord(char) - 32))
        else:
            result.append(char)

    return "".join(result)

def to_lower(sentence):
    result = []
    for char in sentence:
        if 65 <= ord(char) <= 90:
            result.append(chr(ord(char) + 32))
        else:
            result.append(char)
    return "".join(result)

def capitalize(sentence):
    result = ""
    if sentence:
        result += to_upper(sentence[0])
    result += to_lower(sentence[1:])
    return result