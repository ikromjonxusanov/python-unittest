def get_full_name(ism, familiya, otasi=''):
    if otasi:
        return f"{ism} {otasi} {familiya}".title()
    return f"{ism} {familiya}".title()
