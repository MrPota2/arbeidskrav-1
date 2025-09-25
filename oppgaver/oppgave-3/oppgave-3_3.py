def rgb_to_hex(r: int, g: int, b:int) -> str:
    """
    Converts a user-inputted RGB value to its hexadecimal equivalent.
    :param r: Red value (0-255)
    :param g: Green value (0-255)
    :param b: Blue value (0-255)
    :return: Hex color code, format '#RRGGBB'
    """

    for color_value in (red_input, green_input, blue_input):
        if not 0 <= color_value <= 255:
            raise ValueError(f"Wrong value: {color_value} has to be between 0-255.")


    hex_code = '#'
    for color in (r, g, b):
        hex_code += f"{color:02X}"

    print(f"""
RGB values:
Red: {r:>6}
Green: {g:>4}
Blue: {b:>5}
    """)
    # (Yes, having fun with decorators here)


    print()
    print("The hex value is:", hex_code)
    return hex_code


red_input = int(input("Enter the RED color in decimal form\n(0-255): "))
green_input = int(input("Enter the GREEN color in decimal form\n(0-255): "))
blue_input = int(input("Enter the BLUE color in decimal form\n(0-255): "))

rgb_to_hex(red_input, green_input, blue_input)
