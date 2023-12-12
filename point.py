
# coordinates of a pixel
class Cell:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def index(self) -> tuple:
        return (self.x, self.y)
    
    def dist(self, p) -> float:
        return ((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** 0.5
    
    def __eq__(self, __value: object) -> bool:
        return self.x == __value.x and self.y == __value.y
    
    def is_traversable(self, image):
        x, y = image.shape
        if self.y >= x or self.x >= y:
            return False
        return image[self.y][self.x] != 0

    def __str__(self) -> str:
        return f'{self.x} {self.y}'


# содержит информацию о текущей Cell, расстояние от старта и родитель Node
class Node:
    def __init__(self, cell: Cell, g: int, parent) -> None:
        assert isinstance(parent, Node) or parent is None
        self.cell = cell
        self.g = g
        self.parent = parent

# Эвристика
    def priority(self, goal: Cell):
        return self.g + self.cell.dist(goal)

# приоритет Node
    def f_value(self, goal: Cell) -> float:
        return self.g + self.cell.dist(goal)
    
    def index(self):
        return self.cell.index()
    
    def __eq__(self, obj) -> bool:
        if isinstance(obj, Node):
            return self.cell == obj.cell and self.g == obj.g and (self.parent is None and obj.parent is None or self.parent.cell == obj.parent.cell)
        
        if isinstance(obj, Cell):
            return self.cell == obj
    
    def __str__(self) -> str:
        return f'{self.cell}_{round(self.g)}'
    
    def __lt__(self, other):
        assert isinstance(other, Node)
        return self.g < other.g

    # def __eq__(self, other):
    #     assert isinstance(other, Node)
    #     return self.f_value() == other.f_value()