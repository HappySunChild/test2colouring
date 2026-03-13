from tkinter import Frame

class PigmentInput(Frame):
	def update_labels(self):
		...
	
	def get_RYBW(self) -> tuple[float, float, float, float]:
		return (0, 0, 0, 0)
	
	def get_RYBW_ratios(self) -> tuple[float, float, float, float]:
		r, y, b, w = self.get_RYBW()
		total = max(r + y + b + w, 1)
		
		return (r / total, y / total, b / total, w / total)