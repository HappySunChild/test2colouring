from tkinter import Scale, Misc
from typing import Callable

from ...color.flowers import RED_FLOWER, YELLOW_FLOWER, BLUE_FLOWER, WHITE_FLOWER
from .PigmentInput import PigmentInput

SLIDER_WIDTH = 10
SLIDER_LENGTH = 200

class PigmentScales(PigmentInput):
	def __init__(self, master: Misc, onChange: str | Callable) -> None:
		super().__init__(master=master)
		
		red_scale = Scale(self, width=SLIDER_WIDTH, length=SLIDER_LENGTH, showvalue=False, troughcolor=RED_FLOWER.hex, orient="horizontal", command=onChange)
		red_scale.pack(anchor="w")

		yellow_scale = Scale(self, width=SLIDER_WIDTH, length=SLIDER_LENGTH, showvalue=False, troughcolor=YELLOW_FLOWER.hex, orient="horizontal", command=onChange)
		yellow_scale.pack(anchor="w")

		blue_scale = Scale(self, width=SLIDER_WIDTH, length=SLIDER_LENGTH, showvalue=False, troughcolor=BLUE_FLOWER.hex, orient="horizontal", command=onChange)
		blue_scale.pack(anchor="w")

		white_scale = Scale(self, width=SLIDER_WIDTH, length=SLIDER_LENGTH, showvalue=False, troughcolor=WHITE_FLOWER.hex, orient="horizontal", command=onChange)
		white_scale.pack(anchor="w")
		
		self._red_scale = red_scale
		self._yellow_scale = yellow_scale
		self._blue_scale = blue_scale
		self._white_scale = white_scale
	
	def update_labels(self):
		r, y, b, w = self.get_RYBW_ratios()
		
		self._red_scale.configure(label=f"Red - {r * 100:.1f}%")
		self._yellow_scale.configure(label=f"Yellow - {y * 100:.1f}%")
		self._blue_scale.configure(label=f"Blue - {b * 100:.1f}%")
		self._white_scale.configure(label=f"White - {w * 100:.1f}%")
	
	def get_RYBW(self) -> tuple[float, float, float, float]:
		return (self._red_scale.get(), self._yellow_scale.get(), self._blue_scale.get(), self._white_scale.get())