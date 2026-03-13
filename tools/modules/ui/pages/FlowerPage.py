from mixbox import float_rgb_to_latent, latent_to_float_rgb, LATENT_SIZE
from tkinter import Misc, Frame

from ...color.Color import Color
from ...color.Flowers import RED_FLOWER, YELLOW_FLOWER, BLUE_FLOWER, WHITE_FLOWER

from ..Page import Page

from ..components.ColorDisplay import ColorDisplay
from ..components.PigmentEntries import PigmentEntries
from ..components.PigmentScales import PigmentScales
from ..components.PigmentInput import PigmentInput

Z_RED = float_rgb_to_latent(RED_FLOWER.unpack())
Z_YELLOW = float_rgb_to_latent(YELLOW_FLOWER.unpack())
Z_BLUE = float_rgb_to_latent(BLUE_FLOWER.unpack())
Z_WHITE = float_rgb_to_latent(WHITE_FLOWER.unpack())

class FlowerPage(Page):
	def __init__(self, master: Misc) -> None:
		container = Frame(master=master)
		
		self.content = container
		
		_color_display = ColorDisplay(container)
		_color_display.place(x=210, y=5)
		
		_quantized_color_display = ColorDisplay(container, "ColorId Preview")
		_quantized_color_display.place(x=325, y=5)
		
		self._color_display = _color_display
		self._quantized_color_display = _quantized_color_display
		
		self._pigment_entries = PigmentEntries(container, self.update_display)
		self._pigment_scales = PigmentScales(container, self.update_display)
		
		self._active_input = self._pigment_scales
		
		# TODO: allow multiple mixing steps, with optionally with arbitrary colorid inputs.
		
		self.set_active_input(self._pigment_entries)
		self.update_display()
	
	def set_active_input(self, input: PigmentInput):
		if self._active_input:
			self._active_input.pack_forget()
		
		input.pack(anchor="w")
		
		self._active_input = input
	
	def update_display(self, *_):
		r, y, b, w = self._active_input.get_RYBW_ratios()
		
		z_mix = [0.0] * LATENT_SIZE
	
		for i in range(len(z_mix)):
			z_mix[i] = (r * Z_RED[i] +
				y * Z_YELLOW[i] +
				b * Z_BLUE[i] +
				w * Z_WHITE[i])
		
		mixed_color = Color(*latent_to_float_rgb(z_mix))
		
		self._active_input.update_labels()
		
		self._color_display.set_color(mixed_color)
		self._quantized_color_display.set_color(mixed_color.quantized)