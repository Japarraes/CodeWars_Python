def create_phone_number(n):
    
    n_str = ''.join(map(str, n))
    return f"({n_str[:3]}) {n_str[3:6]}-{n_str[6:]}"
