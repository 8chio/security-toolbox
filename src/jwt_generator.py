from base64_tool import encode_base64_urlsafe
import json

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
    jwt_token = f"{encoded_header}.{encoded_payload}"

    return jwt_token

payload = {
    "sub": "1234567890",
    "name": "John Doe",
    "admin": True,
    "iat": 1516239022,
    "nbf": 1516239022,
    "exp": 1516242622
}

print(generate_jwt(payload)) 