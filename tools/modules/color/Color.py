from .ColorId import to_id, from_id
from .ANSI import RESET, background_24bit_sequence

class Color:
	def __init__(self, red: float, green: float, blue: float) -> None:
		self.r = red
		self.g = green
		self.b = blue
	
	def __repr__(self) -> str:
		return f"Color({self.unpack()})"
	
	@classmethod
	def from_id(cls, color_id: int):
		return cls(*from_id(color_id))
	
	@classmethod
	def from_rgb(cls, red: int, green: int, blue: int):
		return cls(red / 255, green / 255, blue / 255)
	
	@property
	def hex(self) -> str:
		return "#{:02X}{:02X}{:02X}".format(*self.unpack_rgb())
	
	@property
	def color_id(self) -> int:
		return to_id(self.unpack())
	
	@property
	def quantized(self):
		return Color.from_id(self.color_id)
	
	def blit(self) -> str:
		return background_24bit_sequence(*self.unpack_rgb()) + "  " + RESET
	
	def unpack_rgb(self) -> tuple[int, int, int]:
		return (round(self.r * 255), round(self.g * 255), round(self.b * 255))
	
	def unpack(self) -> tuple[float, float, float]:
		return (self.r, self.g, self.b)