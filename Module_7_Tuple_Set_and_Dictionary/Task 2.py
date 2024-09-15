names = set()

name_input = input("Please enter a name, press enter to stop: ")


while name_input != "":
    if name_input in names:
        print("Existing name")
    else:
        print("New name")
    names.add(name_input)
    name_input = input("\nPlease enter a name, press enter to stop: ")

