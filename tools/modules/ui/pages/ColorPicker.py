from pyautogui import pixel as get_screen_pixel
from pynput import mouse
from tkinter import Misc, Frame, Button

from ...color.Color import Color

from ..Page import Page

from ..components.ColorDisplay import ColorDisplay

class ColorPickerPage(Page):
	def __init__(self, master: Misc) -> None:
		container = Frame(master=master)
		
		pick_button = Button(master=container, text="Pick Color", command=lambda: self.engage_picker())
		pick_button.pack(anchor="w", padx=5, pady=5)
		
		color_display = ColorDisplay(master=container, label="Picked Color")
		color_display.place(x=210, y=5)
		
		colorid_display = ColorDisplay(master=container, label="Picked ColorId")
		colorid_display.place(x=325, y=5)
		
		self._color_display = color_display
		self._colorid_display = colorid_display
		self._button = pick_button
		
		self.content = container
	
	def engage_picker(self):
		self._button.configure(text="Picking...")
		self._button.update()
		
		pixel_color = Color(0, 0, 0)
		
		def on_click(x, y, _, pressed):
			nonlocal pixel_color
			
			if not pressed:
				return
			
			pixel_color = Color.from_rgb(*get_screen_pixel(x, y))
			
			return False
		
		# start picking
		with mouse.Listener(on_click=on_click) as listener:
			listener.join()
		
		# done picking
		self._button.configure(text="Pick Color")
		
		self._color_display.set_color(pixel_color)
		self._colorid_display.set_color(pixel_color.quantized)
