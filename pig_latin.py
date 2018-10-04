# if the word begins with a letter not in the vowel list,
# remove the first letter of the word and add it to the end of the word
# and add 'ay' after that.

# the program should accept an English word
# the program should print the word translated into pig latin
# assume the word is free of punctuation and capitalization.

def pig_latin(word):
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    first_character = word[0]
    for vowel in vowel_list:
        if first_character == vowel:
            pig_text = word + 'way'
            return pig_text


print("### TESTING ###")
# if the word begins with a vowel (a,e,i,o, u) add 'way' to the end of the word
# script matches vowel
print(pig_latin('awl'))
print(pig_latin('eel'))
print(pig_latin('ice'))
print(pig_latin('owl'))
print(pig_latin('udder'))

