from modules.color.Flowers import RED_FLOWER, YELLOW_FLOWER, BLUE_FLOWER, WHITE_FLOWER, Color
from modules.color.BrickColorIdMap import get_brickcolor
from mixbox import lerp_float as mixbox_lerp
from math import gcd, floor

def percentage_to_fraction(percentage: float) -> tuple[int, int]:
	if percentage == 0:
		return 0, 1
	
	numerator = floor(percentage * 10000) / 10000
	denominator = 1
	
	while numerator % 1 != 0:
		denominator *= 10
		numerator *= 10
	
	factor = gcd(int(numerator), denominator)
	
	return int(numerator) // factor, denominator // factor

def percentage_to_ratio(percentage: float) -> tuple[int, int]: # part : part ratio
	numerator, denominator = percentage_to_fraction(percentage)
	
	return numerator, denominator - numerator

def mix_colors(color_a: Color, color_b: Color, mix_alpha: float) -> Color:
	return Color(*mixbox_lerp(color_a.unpack(), color_b.unpack(), mix_alpha)).quantized

RESOLUTION = 21
COLOR_MAPPING = {
	"Red": Color(1, 0, 0),
	"Green": Color(0, 1, 0),
	"Blue": Color(0, 0, 1),
	
	"Cyan": Color(0, 1, 1),
	"Magenta": Color(1, 0, 1),
	"Yellow": Color(1, 1, 0),
	
	"Red Flower": RED_FLOWER,
	"Yellow Flower": YELLOW_FLOWER,
	"Blue Flower": BLUE_FLOWER,
	"White Flower": WHITE_FLOWER,
}

def run_gradient_prompt():
	color_a = input("Color A: ")
	color_b = input("Color B: ")

	output = f"Gradient from {COLOR_MAPPING[color_a].blit()} '{color_a}' to {COLOR_MAPPING[color_b].blit()} '{color_b}' in {RESOLUTION} intervals\n"

	for x in range(RESOLUTION):
		mix_alpha = x / (RESOLUTION - 1)
		
		mixed_color = mix_colors(COLOR_MAPPING[color_a], COLOR_MAPPING[color_b], mix_alpha)		
		brick = get_brickcolor(mixed_color.color_id)
		
		part_a, part_b = percentage_to_ratio(mix_alpha)
		
		output += f"{mixed_color.blit()} {part_b:2}:{part_a:<2} -> {brick[0]} [{mixed_color.color_id:03}] \n"

	print(output)

while True:
	run_gradient_prompt()
