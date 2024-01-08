# utils/colors.py

class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'

def colorize(text, color):
    """Apply color to text for console output."""
    color_code = getattr(Colors, color.upper(), Colors.RESET)
    return f"{color_code}{text}{Colors.RESET}"
