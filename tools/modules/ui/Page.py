from tkinter import Misc, Widget, Label

class Page:
	def __init__(self, master: Misc) -> None:
		self.content: Widget = Label(master=master, text="DefaultPage")
	
	def show(self):
		self.content.place(x=0, y=0, relwidth=1, relheight=1)
		
	def hide(self):
		self.content.place_forget()