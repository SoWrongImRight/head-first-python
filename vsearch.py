def search4vowels(word:str) -> set:
    """Return any vowels found in supplied word."""
    vowels = set('aeiou')
    return vowels.intersection(set(word))

def search4letters(phrase:str, letters:str='aeiou') -> set:
    """Checks a provided phrase for any of the search letters provided"""
    return set(letters).intersection(set(phrase))
