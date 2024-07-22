from is_prime import is_prime


def test_prime_numbers():
    assert is_prime(2)
    assert is_prime(3)
    assert is_prime(5)
    assert is_prime(7)
    assert is_prime(11)


def test_non_prime_numbers():
    assert not is_prime(1)
    assert not is_prime(4)
    assert not is_prime(6)
    assert not is_prime(8)
    assert not is_prime(9)
    assert not is_prime(10)


def test_negative_numbers():
    assert not is_prime(-1)
    assert not is_prime(-10)
