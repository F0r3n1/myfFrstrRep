class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        self.x = x
        self.y = y

    def get_coord(self):
        return self.x,self.y

    @classmethod
    def set_mincoord(clc,mincoord):
        clc.MIN_COORD=mincoord


Point.set_mincoord(200)
print(Point.MIN_COORD)