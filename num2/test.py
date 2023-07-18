command = input("What are you doing next? ")

match command.split():
    case ["quit"]:  # введено одно слово "quit"
        print("Goodbye!")
    case ["look"]:  # введено одно слово "look"
        print('look')
