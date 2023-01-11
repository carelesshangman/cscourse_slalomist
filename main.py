class Steza:
    def __init__(self, width, height, obstacles):
        self.width = width
        self.height = height
        self.obstacles = obstacles

    def zaprto(self, x, y):
        for obstacle in self.obstacles:
            y0, x0, x1 = obstacle
            if y == y0 and x0 <= x <= x1:
                return True
        return False

    def konec(self, x, y, smer):
        if smer == '<':
            while x > 1 and not self.zaprto(x-1, y):
                x -= 1
        elif smer == '>':
            while x < self.width and not self.zaprto(x+1, y):
                x += 1
        elif smer == '^':
            while y > 1 and not self.zaprto(x, y-1):
                y -= 1
        elif smer == 'v':
            while y < self.height and not self.zaprto(x, y+1):
                y += 1
        return x, y

# Create a cycling path with width 10 and height 5, and an obstacle at (2, 3, 7)
steza = Steza(10, 5, [(2, 3, 7)])

# Check if the field (4, 2) is covered by an obstacle
print(steza.zaprto(4, 2))  # Output: True

# Check where the cyclist will end up if they start at (1, 1) and move to the right
print(steza.konec(1, 1, '>'))  # Output: (10, 1)

# Check where the cyclist will end up if they start at (4, 2) and move down
print(steza.konec(4, 2, 'v'))  # Output: (4, 5)
