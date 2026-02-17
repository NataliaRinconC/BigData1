import pytest
from Primero import es_primo


def test_numeros_primos():
    assert es_primo(2) == True
    assert es_primo(3) == True
    assert es_primo(5) == True
    assert es_primo(11) == True

def test_numeros_no_primos():
    assert es_primo(1) == False
    assert es_primo(4) == False
    assert es_primo(6) == False
    assert es_primo(9) == False
    assert es_primo(0) == False
    assert es_primo(-3) == False
