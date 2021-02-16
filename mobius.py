'''

Möbius function: 

For any positive integer n,n, define μ(n)μ(n) as the sum of the primitive n^\text{th}nth roots of unity.

It has values in \{-1, 0, 1\}{−1,0,1} depending on the factorization of nn into prime factors:

a) \mu(n) = 1μ(n)=1 if nn is a square-free positive integer with an even number of prime factors.
b) \mu(n) = -1μ(n)=−1 if nn is a square-free positive integer with an odd number of prime factors.
c) \mu(n) = 0μ(n)=0 if nn has a squared prime factor.

'''

import math


def isSquareRoot(num):
    '''
    Checks whether the input num is a square root or not.
    Output is a boolean.
    '''
    try:
        num_sqrt = math.sqrt(num)
        if int(num_sqrt)**2 == num:
            return True
        else:
            return False

    except Exception as e:
        return('Error in finding Square Root:' + str(e))


def get_factors(num):
    try:
        '''
        outputs the factors between 1 and num excluding both
        eg: for 8 -> [2,4,8]
        '''
        factors = []
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                factors.append(i)

        factors.append(num)

        return factors

    except Exception as e:
        return('Error in getting factors: ' + str(e))


def isPrime(num):
    '''
    Checks whether the input num is a prime or not
    output is a boolean 
    '''
    try:
        if num < 2:
            return False
        else:
            for i in range(2, num):
                if (num % i == 0):
                    return False
            return True

    except Exception as e:
        return ('Error in evaluating prime number: ' + str(e))


def Mobius(num):
    '''
    Returns the mobius value of a number.
    '''
    try:
        exp = ''

        if num <= 0:
            exp = f'Number can\'t be zero or negative.'
            return {'val': None, 'exp' : exp}
        if num == 1:
            exp = f'The Möbius Value of number 1 is 1.'
            return {'val': 1, 'exp' : exp}
        
        factors = get_factors(num)

        prime_count = 0
        prime_numbers = []
        for i in factors:
            if isSquareRoot(i):
                exp ="The number {} can be divided by {} which is a perfect square.".format(num,i)
                return {'val': 0, 'exp' : exp}
            elif isPrime(i):
                prime_numbers.append(i)
                prime_count += 1

        exp = 'The number {} can be get by multiplying {}.'.format(num,prime_numbers)
        if (prime_count % 2 != 0):
            return {'val': -1, 'exp' : exp}
        else:
            return {'val': 1, 'exp' : exp}

    except Exception as e:
        return ('Error Finding Möbius function: ' + str(e))
                


if __name__ == '__main__':
    n = int(input("Enter a number to get it's mobius value: "))
    op = Mobius(n)
    print('Mobius Value = {} \nExplaination: {}'.format(op['val'], op['exp']))
