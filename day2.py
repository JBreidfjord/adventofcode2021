from dataclasses import dataclass


@dataclass
class Submarine:
    position: int = 0
    depth: int = 0
    aim: int = 0

    def move(self, magnitude: int, direction: str):
        if direction == "up":
            self.aim -= magnitude
        elif direction == "down":
            self.aim += magnitude
        elif direction == "forward":
            self.position += magnitude
            self.depth += magnitude * self.aim

    def mult(self):
        return self.position * self.depth


with open("day2_input") as f:
    orders = [o.split(" ") for o in f.readlines()]

orders = [(d, int(m)) for d, m in orders]
submarine = Submarine()
for (direction, magnitude) in orders:
    submarine.move(magnitude, direction)

print(submarine.mult())
