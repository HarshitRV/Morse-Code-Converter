from morse import MorseCode

translate = MorseCode()

# English to morse
text = input("enter a message : ")

morse_code = translate.to_morse(text)

print(morse_code)

# Morse to english
text = input("enter morse code: ")

english_text = translate.to_english(text)

print(english_text)