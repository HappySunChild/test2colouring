from tkinter import Frame, Label, Misc

from ...color.Color import Color
from ...color.BrickColorIdMap import get_brickcolor

class ColorDisplay(Frame):
	def __init__(self, master: Misc, label: str = "Color Preview") -> None:
		super().__init__(master=master)
		self.pack_propagate(False)
		
		display = Frame(master=master, width=100, height=100, bg="black", borderwidth=1, relief="solid")
		display.place(in_=self, y=14)
		
		info_text = Label(master=master, wraplength=100)
		info_text.place(in_=display, rely=1, y=1)
		
		name_label = Label(master=master, text=label)
		name_label.place(in_=display, y=-22, x=-3)
		
		self.display = display
		self.label = info_text
	
	def set_color(self, color: Color) -> None:
		closest_brickcolor = get_brickcolor(color.color_id)
		
		self.label.configure(text=f"{closest_brickcolor[0]} - {color.color_id}")
		self.display.configure(bg=color.hex)