from fizzbuzz import fizzbuzz 


# Test function
def test_fizzbuzz():
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(31) == "31"
    assert fizzbuzz(60) == "FizzBuzz"
    assert 9 == 4


test_fizzbuzz()