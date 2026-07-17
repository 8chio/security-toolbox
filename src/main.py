from password_generator import generate_password

print("=== Security Toolbox ===")
print("1. Password Generator")
print("2. SHA256 Hash")
print("0. Exit")

menu = input("Select > ")

if menu == "1":
    print("Password Generator를 선택했습니다.")
    length = int(input("Enter the desired password length: "))
    password = generate_password(length)
    print(f"Generated Password: {password}")

elif menu == "2":
    print("SHA256 Hash를 선택했습니다.")

elif menu == "0":
    print("프로그램을 종료합니다.")

else:
    print("잘못된 메뉴입니다.")