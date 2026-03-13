from modules.color.BrickColorIdMap import get_brickcolor
from modules.color.Color import Color

target_brickcolor = input("BrickColor: ")

for id in range(1000):
	brickcolor = get_brickcolor(id)
	
	if brickcolor[0] == target_brickcolor:
		color = Color.from_id(id)
		
		print(f"{color.blit()} {id}")