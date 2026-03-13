from modules.color.Color import Color
from modules.color.BrickColors import get_closest_brickcolor

color = Color.from_id(int(input("Color id: ")))
brickcolor = get_closest_brickcolor(color.unpack_rgb())

print(color.color_id, brickcolor.name)