def main():
    hello("world")
    goodbye("world")


def hello(name):
    print(f"hello, {name}")


def goodbye(name):
    print(f"goodbye, {name}")


if (
    __name__ == "__main__"
):  # Pour pas que le main soit lu à chaque fois (c’est uniquement pour le tests, donc quand on lance le fichier en lui même)
    main()
