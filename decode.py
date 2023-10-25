# Marvens
def decode(passcode):
    decoded_passcode = []
    for i in range(len(passcode)):
        decoded_passcode.append(str(int(passcode[i]) - 3))
    decoded_passcode = ''.join(decoded_passcode)
    return decoded_passcode