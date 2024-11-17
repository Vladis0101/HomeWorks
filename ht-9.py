import re

def check_login(login: str) -> bool:

    if len(login) < 5 or len(login) > 20:
        return False

    if not re.match(r'^[a-zA-Z0-9_]+$', login):
        return False

    return True

print(check_login("User_123"))
print(check_login("lu"))
print(check_login("user@123"))


def check_phone(phone: str) -> bool:
    pattern = r'^\+375\((29|33|44|25)\)\d{3}-\d{2}-\d{2}$'
    if re.match(pattern, phone):
        return True
    return False

print(check_phone("+375(29)123-45-67"))
print(check_phone("+375(33)987-12-34"))
print(check_phone("+375(25)123-45-67"))
print(check_phone("+375(50)123-45-67"))
print(check_phone("+375(29)123-4567"))
