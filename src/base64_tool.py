import base64

def encode_base64(input_string):
    encoded_bytes = base64.b64encode(input_string.encode("utf-8"))
    return encoded_bytes.decode("utf-8")

def decode_base64(encoded_string):
    decoded_bytes = base64.b64decode(encoded_string.encode("utf-8"))
    return decoded_bytes.decode("utf-8")

def decode_base64_urlsafe(encoded_string):
    padding = '=' * (-len(encoded_string) % 4)  # Add padding if necessary
    encoded_string += padding
    decoded_bytes = base64.urlsafe_b64decode(encoded_string.encode("utf-8"))
    return decoded_bytes.decode("utf-8")

def encode_base64_urlsafe(input_string):
    if isinstance(input_string, str):
        input_string = input_string.encode("utf-8")
    encoded_bytes = base64.urlsafe_b64encode(input_string)
    return encoded_bytes.decode("utf-8").rstrip('=')  # Remove padding for URL-safe encoding