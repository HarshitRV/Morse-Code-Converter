from data import morse_code

class MorseCode:
    def __init__(self):
        self.in_morse = ""
    
    def to_morse(self, sentence):
        sentence = sentence.split(" ")

        morse_translation = []
        for word in sentence:
            word = list(word)

            for letter in word:
                morse_translation.append(morse_code[letter.lower()])

            morse_translation.append("     ")

        self.in_morse = "   ".join(morse_translation)

        return self.in_morse

    # def to_message(self, morse_code):