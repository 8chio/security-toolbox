from base64_tool import decode_base64_urlsafe
import json

def decode_jwt(token):
    parts = token.split('.')
    if len(parts) != 3:
        raise ValueError("Invalid JWT format. A valid JWT must have three parts separated by dots.")
    
    # Split the JWT into its three parts
    header, payload, signature = parts

    decode_header = decode_base64_urlsafe(header)
    decode_payload = decode_base64_urlsafe(payload)

    header_dict = json.loads(decode_header)  # Validate header is valid JSON
    payload_dict = json.loads(decode_payload)  # Validate payload is valid JSON
    
    return header_dict, payload_dict, signature