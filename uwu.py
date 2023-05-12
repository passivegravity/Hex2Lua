import colorama
from colorama import Fore, Style

# Initialize colorama
colorama.init()

def hex_to_lua(hex_value):
    # Remove the '#' symbol if present
    if hex_value.startswith('#'):
        hex_value = hex_value[1:]

    # Split the hexadecimal value into RGB components
    r = int(hex_value[0:2], 16)
    g = int(hex_value[2:4], 16)
    b = int(hex_value[4:6], 16)

    # Format the Lua-compatible color value
    lua_color = f"0x{(r << 16) | (g << 8) | b:06X}"
    return lua_color, (r, g, b)

# Define colorama styles
input_prompt_style = Fore.CYAN + Style.BRIGHT
output_style = Fore.GREEN + Style.BRIGHT

# Ask the user to enter a hex value
hex_color = input(input_prompt_style + "Enter a hexadecimal color value: " + Style.RESET_ALL)

# Convert the hex value to Lua-compatible format and get the RGB values
lua_color, rgb_values = hex_to_lua(hex_color)

# Print the converted value and RGB values
print(output_style + "Lua-compatible color value:" + Style.RESET_ALL, lua_color)
print(output_style + "RGB values:" + Style.RESET_ALL, rgb_values)

# Reset colorama styles
colorama.deinit()
