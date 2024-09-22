import sys


def meow(n: int) -> str:
    """
    Meow n times.
    :param n: Number of times to meow
    :type n: int
    :raise TyperError: If n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    """
    return "meow\n" * n


number = int(input("Number: "))
print(meow(number), end="")

if len(sys.argv) == 1:
    print("meow")
else:
    print("usage: meows.py")
