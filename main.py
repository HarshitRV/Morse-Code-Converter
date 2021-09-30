from morse import MorseCode

encode = MorseCode()

message = input("Enter a message: ")

encoded_message = encode.to_morse(message)

print(encoded_message)