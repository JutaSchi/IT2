ordbok={'a': 'c', 'b': 'd', 'c': 'e', 'd': 'f', 'e': 'g', 'f': 'h', 'g': 'i', 'h': 'j', 'i': 'k', 'j': 'l', 'k': 'm', 'l': 'n', 'm': 'o', 'n': 'p', 'o': 'q', 'p': 'r', 'q': 's', 'r': 't', 's': 'u', 't': 'v', 'u': 'w', 'v': 'x', 'w': 'y', 'x': 'z', 'y': 'a', 'z': 'b', 'ø': 'a', 'å': 'b'}
tekst="Jeg elsker Linus Torvalds" 
resultat = ''.join(ordbok.get(bokstav, bokstav) for bokstav in tekst.lower())
print(resultat)