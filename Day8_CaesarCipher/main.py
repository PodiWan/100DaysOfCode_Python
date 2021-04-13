enc_dec = 0 # 0 = encode, 1 = decode

while True:

    user_input =  input("Type \'encode\' to encrypt, \'decode\' to decrypt: ")

    if user_input != "encode" and user_input != "decode":
        exit("Invalid input!")

    if user_input == "encode":
        enc_dec = 0
    else:
        enc_dec = 1

    message_input = input("Input the message: ")
    shift_input = int(input("Type the shift number: "))
    message_output = ""


    for i in range(len(message_input)):
        message_output += chr(ord(message_input[i]) + shift_input) if enc_dec == 0 else chr(ord(message_input[i]) - shift_input)

    print(message_output)