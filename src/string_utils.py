def print_string(text):
    if not isinstance(text, str):
        print("Помилка: аргумент має бути рядком (str).")
        return
    print(text)

def check_case(text):
    if not isinstance(text, str):
        print("Помилка: аргумент має бути рядком (str).")
        return
    if text.isupper():
        print("Всі літери великі.")
    elif text.islower():
        print("Всі літери малі.")
    else:
        print("Регістр змішаний.")
