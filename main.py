from morse import MorseCode

translate = MorseCode()

message = input("Enter a message: ")

encoded_message = translate.to_morse(message)

print(encoded_message)

decode = encoded_message

decoded_message = translate.to_english(decode)

print(decoded_message)