from re import A


def create_phone_number(n):

    pref = "".join(str(i) for i in (n[0:3]))
    num1 = "".join(str(i) for i in (n[3:6]))
    num2 = "".join(str(i) for i in (n[6:]))
    
    return f"({pref}) {num1}-{num2}"
