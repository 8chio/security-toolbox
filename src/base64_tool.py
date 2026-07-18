import base64

def encode_base64(input_string):
    encoded_bytes = base64.b64encode(input_string.encode("utf-8"))
    return encoded_bytes.decode("utf-8")

def decode_base64(encoded_string):
    decoded_bytes = base64.b64decode(encoded_string.encode("utf-8"))
    return decoded_bytes.decode("utf-8")