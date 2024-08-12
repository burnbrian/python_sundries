import base64

# Decode the data
def decode_first_chars_base64(s):
    # Extract first character of each word
    first_chars = ''.join(word[0] for word in s.split())
    # Base64 padding
    first_chars += '=' * ((4 - len(first_chars) % 4) % 4)
    # Print Base64
    print(f"Base64: {first_chars} \n")
    # Decode
    decoded_string = base64.b64decode(first_chars).decode('utf-8')
    return decoded_string

# Do things
with open('wireshark.txt', 'r') as file:
    i = 0
    for line in file:
        print(f"--- Request {i} --- \n")
        print(decode_first_chars_base64(line))
        i += 1