def not_vowel(character):
    vowelOrds = [97, 101, 105, 111, 117, 65, 69, 73, 79, 85]
    state = True

    for i in vowelOrds:
        if ord(str(character)) == i:
            state = False
    return state
