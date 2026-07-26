from base64_tool import encode_base64_urlsafe
import hashlib
import hmac

#secret_key = "my_secret_key"  # Replace with your actual secret key for signing the JWT

def verify_jwt(token, secret_key):
    parts = token.split('.')
    if len(parts) != 3:
        return False, "Invalid token format."
    header = parts[0]
    payload = parts[1]
    signature = parts[2]
    message = f"{header}.{payload}".encode('utf-8')
    expected_signature = hmac.new(secret_key.encode('utf-8'), message, hashlib.sha256).digest()
    encoded_expected_signature = encode_base64_urlsafe(expected_signature)
    if signature != encoded_expected_signature:
        return False, "Invalid signature."
    return True, "Token is valid."

# print(verify_jwt("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJob2siLCJuYW1lIjoiSG8gSyIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTc1MDAwMDAwMCwibmJmIjoxNzUwMDAwMDAwLCJleHAiOjE3NTAwMDM2MDB9.jHeGi5uKTHy7PKd6G_A7DrBxf6qnxPko568khr8qf5o", secret_key))
