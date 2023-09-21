def fizzBuzz(number):
    no_remainder_3 = not bool(number%3)
    no_remainder_5 = not bool(number%5)
    if no_remainder_3 and no_remainder_5:
        return "Fizz Buzz"
    elif no_remainder_3:
        return "Fizz"
    elif no_remainder_5:
        return "Buzz"
    else:
        return str(number)


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert fizzBuzz(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert fizzBuzz(6) == "Fizz", "6 is divisible by 3"
    assert fizzBuzz(5) == "Buzz", "5 is divisible by 5"
    assert fizzBuzz(7) == "7", "7 is not divisible by 3 or 5"
