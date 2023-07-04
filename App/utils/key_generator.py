from string import (
    ascii_lowercase,
    ascii_uppercase,
    digits,
    punctuation
)
from random import choice


def keyGenerator(length : int = 10):
    symbols : str = ascii_lowercase + ascii_uppercase + digits + punctuation
    
    secret_key : str = "".join(
        [ choice(symbols) for i in range(length) ]
    )
    return secret_key