from typing import Callable
from tkinter import Entry, Label, Misc, IntVar

from ...color.flowers import RED_FLOWER, YELLOW_FLOWER, BLUE_FLOWER, WHITE_FLOWER
from .PigmentInput import PigmentInput

ENTRY_WIDTH = 30

class PigmentEntry(Entry):
	def __init__(self, master: Misc, changeCallback: Callable, fg: str, bg: str, vcmd: tuple[str, str]):
		text_variable = IntVar(master, 0)
		text_variable.trace_add("write", callback=lambda a, b, c, d=text_variable: changeCallback(None))
		
		super().__init__(
			master=master,
			width=ENTRY_WIDTH,
			fg=fg,
			bg=bg,
			textvariable=text_variable,
			vcmd=vcmd,
			validate="key"
		)

class PigmentEntries(PigmentInput):
	def __init__(self, master: Misc, callback: Callable):
		super().__init__(master=master, padx=5, pady=5)
		
		vcmd = (self.register(lambda p: str.isdigit(p) or p == ""), "%P")
		
		red_entry = PigmentEntry(
			master=self,
			changeCallback=callback,
			bg=RED_FLOWER.hex,
			fg="white",
			vcmd=vcmd
		)
		red_entry.pack(anchor="w", padx=0, pady=1)
		
		yellow_entry = PigmentEntry(
			master=self,
			changeCallback=callback,
			bg=YELLOW_FLOWER.hex,
			fg="black",
			vcmd=vcmd,
		)
		yellow_entry.pack(anchor="w", padx=0, pady=1)
		
		blue_entry = PigmentEntry(
			master=self,
			changeCallback=callback,
			bg=BLUE_FLOWER.hex,
			fg="white",
			vcmd=vcmd,
		)
		blue_entry.pack(anchor="w", padx=0, pady=1)
		
		white_entry = PigmentEntry(
			master=self,
			changeCallback=callback,
			bg=WHITE_FLOWER.hex,
			fg="black",
			vcmd=vcmd,
		)
		white_entry.pack(anchor="w", padx=0, pady=1)
		
		ratio_label = Label(master=self, justify="left")
		ratio_label.pack(anchor="w")
		
		self._label = ratio_label
		
		self._red_entry = red_entry
		self._yellow_entry = yellow_entry
		self._blue_entry = blue_entry
		self._white_entry = white_entry
	
	def update_labels(self):
		r, y, b, w = self.get_RYBW_ratios()
		
		self._label.configure(text=f"Ratios:\n{r*100:.2f}% Red\n{y*100:.2f}% Yellow\n{b*100:.2f}% Blue\n{w*100:.2f}% White")
	
	def get_RYBW(self) -> tuple[int, int, int, int]:
		return (
			int(self._red_entry.get() or 0),
			int(self._yellow_entry.get() or 0),
			int(self._blue_entry.get() or 0),
			int(self._white_entry.get() or 0)
		)