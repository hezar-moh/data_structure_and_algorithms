def factorize(number):
    factors = []
    divisor = 2
    while number >= divisor:
        while number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        divisor += 1
    return factors

if __name__ == "__main__":
    print(factorize(28)) 
    print(factorize(50))
    print(factorize(13))
