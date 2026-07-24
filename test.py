import json

payload = {
    "sub": "1234567890",
    "name": "John Doe",
    "admin": True,
    "iat": 1516239022,
    "nbf": 1516239022,
    "exp": 1516242622
}

payload_json = json.dumps(payload, separators=(',', ':'))
print("Payload JSON:", payload_json)

payload123 = json.loads(payload_json)
print("sub:", payload123.get("sub"))
print("name:", payload123.get("name"))
print("admin:", payload123.get("admin"))
print("iat:", payload123.get("iat"))
print("nbf:", payload123.get("nbf"))
print("exp:", payload123.get("exp"))