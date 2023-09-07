def euro(number: float | int) -> str | bool:
    """
    Convert a number of type "float" or of type "int" into a string
    in the euro currency format.

    Args:
        - number: float | int:
            - The number you want to convert.
    
    Returns:
        - str | bool
            - If it returns a string, that's your euro string
            - If it returns a bool (False), something went wrong!
    """
    
    if type(number) == int:
        number_str = str(number)
        number_str += ",- €"
        return number_str
    elif type(number) == float:
        number_list = str(number).split(".")
        if len(number_list[1]) > 2:
            return False
        if len(number_list[1]) < 2:
            number_list[1] += "0"
        number_str = f"{number_list[0]},{number_list[1]} €"
        return number_str
    else:
        return False

def __test():
    while True:
        flt = input("> Float: ")
        try:
            flt = float(flt)
        except TypeError:
            print("Not a float")
            exit(0)
        print(euro(flt))

if __name__ == "__main__":
    __test()