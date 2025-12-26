def transform_alphabet_to_number(input: str):
    char_list = list(input.upper()) # make sure input is upper case.
    # transform list of character to list of ascii code.
    number_list = [ord(char) for char in char_list]
    return number_list

def transform_number_to_string(input_list: list):
    char_list = [chr(num_code) for num_code in input_list]
    return ''.join(char_list)

def shift_logic(ascii_code: int, shift_position: int):
    shift_position = shift_position % 26 # use mod to handle case shift_position > 26
    res = ascii_code - shift_position
    # if shifted value goes beyond 'A'
    if res < 65:
        res += 26
    # if shifted value goes beyond 'Z'
    if res > 90:
        res -= 26
    return  res

def simpleCipher(encrypted: str, k: int):
    ascii_list = transform_alphabet_to_number(encrypted)
    shift_list = [shift_logic(code, k) for code in ascii_list]
    return transform_number_to_string(shift_list)

def main():
    encrpyted_text = 'VTAOG'
    k = 2
    decrypted_text = simpleCipher(encrpyted_text, k)
    print(decrypted_text)

if __name__=="__main__":
    main()
