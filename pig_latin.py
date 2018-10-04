# the program should accept an English word
# the program should print the word translated into pig latin
# assume the word is free of punctuation and capitalization.

def pig_latin(word):

    if word.startswith(('a', 'e', 'i', 'o', 'u')):
        pig_text = word + 'way'
        return pig_text
    else:
        first_letter = word[0]
        pig_text = word[1:] + first_letter + 'ay'
        return pig_text


# print("### TESTING ###")
# print(pig_latin('awl'))
# print(pig_latin('eel'))
# print(pig_latin('ice'))
# print(pig_latin('owl'))
# print(pig_latin('udder'))
# # # if the word begins with a letter not in the vowel list,
# # remove the first letter of the word and add it to the end of the word
# # and add 'ay' after that.
# print(pig_latin('mudder'))
# print(pig_latin('butter'))
# print(pig_latin('cat'))
# print(pig_latin('train'))
