class Position:
    def __init__(self, x: int, y: int = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"координата по X: {self.x} \nкоордината по Y: {self.y}"

