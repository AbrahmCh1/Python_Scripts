def colored(fg_color, bg_color, text):
    r, g, b = fg_color
    result = f'\033[38;2;{r};{g};{b}m{text}'
    r, g, b = bg_color
    result = f'\033[48;2;{r};{g};{b}m{result}\033[0m'
    return result



print(colored((255,0,0), (0,0,255),"Hola Mundo"))

