RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
STRIKETHROUGH = "\033[7m"

def foreground_24bit_sequence(red: int, green: int, blue: int) -> str:
	return f"\033[38;2;{red};{green};{blue}m"

def background_24bit_sequence(red: int, green: int, blue: int) -> str:
	return f"\033[48;2;{red};{green};{blue}m"