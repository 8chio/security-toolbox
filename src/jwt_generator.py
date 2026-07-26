from base64_tool import encode_base64_urlsafe
import json
import hashlib
import hmac

secret_key = "my_secret_key"  # Replace with your actual secret key for signing the JWT

header = {
    "alg": "HS256",
    "typ": "JWT"
}

def generate_jwt(payload):
    # Convert header and payload to JSON strings
    header_json = json.dumps(header, separators=(',', ':'))
    payload_json = json.dumps(payload, separators=(',', ':'))

    # Encode header and payload using Base64 URL-safe encoding
    encoded_header = encode_base64_urlsafe(header_json)
    encoded_payload = encode_base64_urlsafe(payload_json)

    # Create the JWT by concatenating the encoded header and payload
    message = f"{encoded_header}.{encoded_payload}".encode('utf-8')

    # Sign the message using the secret key
    signature = hmac.new(secret_key.encode('utf-8'), message, hashlib.sha256).digest()
    encoded_signature = encode_base64_urlsafe(signature)

    # Combine the header, payload, and signature to form the final JWT
    jwt_token = f"{encoded_header}.{encoded_payload}.{encoded_signature}"

    return jwt_token