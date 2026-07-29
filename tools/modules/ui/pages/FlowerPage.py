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
		
		color_display = ColorDisplay(container)
		color_display.place(x=210, y=5)
		
		quantized_color_display = ColorDisplay(container, "ColorId Preview")
		quantized_color_display.place(x=325, y=5)
		
		self.color_display = color_display
		self.quantized_color_display = quantized_color_display
		
		self.pigment_entries = PigmentEntries(container, self.update_display)
		self.pigment_scales = PigmentScales(container, self.update_display)
		
		self.active_input = self.pigment_scales
		
		# TODO: allow multiple mixing steps, with optionally with arbitrary colorid inputs.
		
		self.set_active_input(self.pigment_scales)
		self.update_display()
	
	def set_active_input(self, input: PigmentInput):
		if self.active_input:
			self.active_input.pack_forget()
		
		input.pack(anchor="w")
		
		self.active_input = input
	
	def update_display(self, *_):
		r, y, b, w = self.active_input.get_RYBW_ratios()
		
		z_mix = [0.0] * LATENT_SIZE
	
		for i in range(len(z_mix)):
			z_mix[i] = (r * Z_RED[i] +
				y * Z_YELLOW[i] +
				b * Z_BLUE[i] +
				w * Z_WHITE[i])
		
		mixed_color = Color(*latent_to_float_rgb(z_mix))
		
		self.active_input.update_labels()
		
		self.color_display.set_color(mixed_color)
		self.quantized_color_display.set_color(mixed_color.quantized)