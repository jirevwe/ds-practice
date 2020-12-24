def add(first, second):
    """
    :param first: an integer
    :param second: an integer
    :returns: The sum of the two numbers
    """
    if second == None:
        raise TypeError('Supply all parameters')
    return first + second


def power(number, exponent):
    """
    :param number: a positive integer
    :param exponent: a positive integer
    :returns: The power of the number to the exponent
    :raises: TypeError if the number or exponent are less than 0
    """
    if exponent < 0 or number < 0:
        raise TypeError('The number must be more than 0')
    return number**exponent
