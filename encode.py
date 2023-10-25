# Quentin Wright

def encode(password):
    return "".join([str((int(x) + 3) % 10) for x in password])
