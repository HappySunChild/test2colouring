from math import floor

SAMPLE_COUNT = 10

def to_id(color: tuple[float, float, float]) -> int:
	n = SAMPLE_COUNT - 1
	
	red, green, blue = color
	
	return round(red * n) + round(green * n) * SAMPLE_COUNT + round(blue * n) * SAMPLE_COUNT ** 2

def from_id(id: int) -> tuple[float, float, float]:
	n = SAMPLE_COUNT - 1
	
	return (
		floor(id % SAMPLE_COUNT) / n, 
		floor(id % SAMPLE_COUNT ** 2 / SAMPLE_COUNT) / n, 
		floor(id / SAMPLE_COUNT ** 2) / n
	)