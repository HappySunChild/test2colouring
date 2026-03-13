from tkinter import Tk, Menu

from .pages.FlowerPage import FlowerPage
from .pages.ColorPicker import ColorPickerPage

from .Page import Page

class PageManager:
	def __init__(self) -> None:
		self.pages = {}
		self.active_page = None
	
	def add_page(self, index: str, page: Page):
		self.pages[index] = page
		
		if self.active_page == None:
			self.navigate(index)
	
	def navigate(self, index: str):
		new_page: Page = self.pages[index]
		
		if self.active_page == new_page:
			return
		
		if self.active_page:
			self.active_page.hide()
		
		new_page.show()
		
		self.active_page = new_page

class App(Tk):
	def __init__(self) -> None:
		super().__init__()
		
		self.title("Pigment Mixing")
		self.geometry("440x200")
		self.resizable(False, False)
		self.attributes("-topmost", True)
		
		flower_page = FlowerPage(self)
		color_picker_page = ColorPickerPage(self)
		
		page_manager = PageManager()
		page_manager.add_page("flower_mixer", flower_page)
		page_manager.add_page("color_picker", color_picker_page)
		
		app_menubar = Menu(self)
		
		page_menu = Menu(app_menubar, tearoff=False)
		page_menu.add_command(label="Flower Mixer", command=lambda: page_manager.navigate("flower_mixer"))
		page_menu.add_command(label="Color Picker", command=lambda: page_manager.navigate("color_picker"))
		app_menubar.add_cascade(label="Pages", menu=page_menu)
		
		self.configure(menu=app_menubar)