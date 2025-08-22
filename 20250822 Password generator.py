import random
kleine_letters = "abcdefghijklmnopqrstuvwxyz"
hoofdletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cijfers = "0123456789"
tekens = "~!@#$%^&*()_+"
alle_tekens = kleine_letters + hoofdletters + cijfers + tekens

def generatePassword(length):
    password = []
    if length != 12:
        length = 12
    password.append(kleine_letters[random.randint(0,25)])
    password.append(hoofdletters[random.randint(0,25)])
    password.append(cijfers[random.randint(0,9)])
    password.append(tekens[random.randint(0,12)])

    while len(password) < 12:
        password.append(alle_tekens[random.randint(0,74)])
    random.shuffle(password)
    password = ''.join(password)
    return password


password = generatePassword(12)
print("Je wachtwoord is:", password)
