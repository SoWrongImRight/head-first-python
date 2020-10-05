def search4vowels(word:str) -> set:
    """Return any vowels found in supplied word."""
    vowels = set('aeiou')
    return vowels.intersection(set(word))
    