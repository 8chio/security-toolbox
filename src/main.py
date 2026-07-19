from password_generator import generate_password
from hash_generator import generate_sha256_hash
from base64_tool import encode_base64, decode_base64
from jwt_decoder import decode_jwt
import json

print("=== Security Toolbox ===")
print("1. Password Generator")
print("2. SHA256 Hash")
print("3. Base64 Encoder")
print("4. Base64 Decoder")
print("5. JWT Decoder")
print("0. Exit")

menu = input("Select > ")

if menu == "1":
    print("Password Generator를 선택했습니다.")
    length = int(input("Enter the desired password length: "))
    password = generate_password(length)
    print(f"Generated Password: {password}")

elif menu == "2":
    print("SHA256 Hash를 선택했습니다.")
    input_string = input("Enter the string to hash: ")
    hash_value = generate_sha256_hash(input_string)
    print(f"SHA256 Hash: {hash_value}")

elif menu == "3":
    print("Base64 Encoder를 선택했습니다.")
    input_string = input("Enter the string to encode: ")
    encoded_string = encode_base64(input_string)
    print(f"Encoded String: {encoded_string}")

elif menu == "4":
    print("Base64 Decoder를 선택했습니다.")
    encoded_string = input("Enter the Base64 encoded string to decode: ")
    decoded_string = decode_base64(encoded_string)
    print(f"Decoded String: {decoded_string}")

elif menu == "5":
    print("JWT Decoder를 선택했습니다.")
    token = input("Enter the JWT token to decode: ")
    try:
        header, payload, signature = decode_jwt(token)
        print("Header:")
        print(json.dumps(header, indent=4, ensure_ascii=False))
        print("Payload:")
        print(json.dumps(payload, indent=4, ensure_ascii=False))
        print("Signature:") 
        print(signature)
    except ValueError as e:
        print(e)

elif menu == "0":
    print("프로그램을 종료합니다.")

else:
    print("잘못된 메뉴입니다.")