

def client():
    """ This will call the client class"""


def server():
    """This function will call the server class"""


def error():
    print("Please enter the correct value")


def end():
    print("Goodbye!")


def main():
    switch = {
        1: client,
        2: server,
        3: end,

    }
    num = input("1. Cilent\n2. Server\n3. Exit\n")
    switch.get(num, error)()


if __name__ == "__main__":
    main()
