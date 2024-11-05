class Homan():

    head: int
    hands: int
    name: str
    sex: bool

    def __init__(self, v_name):
        self.head = 1
        self.hands = 2
        self.name = v_name

    def __str__(self):
        return f'name = {self.name}'

class Child(Homan):

    def __init__(self, v_name):
        super().__init__(v_name)
        self.name = v_name
        self.coord = 0

    def change_coord(self, v_coord):
        self.coord = v_coord

    def show_coord(self):
        return(self.coord)

    def __str__(self):
        return self.name

class Bus():

    def __init__(self):
        self.l1 = list()

    def add_child(self, ch: Child):
        self.l1.append(ch)

    def del_child(self, ch: Child):
        self.l1.pop(ch)

    def change_coord(self, v_coord):
        for ch in self.l1:
            ch.change_coord(v_coord)

    def show_passangers(self):
        for ch in self.l1:
            print(ch)

    def show_coord_by_passengers(self):
        for ch in self.l1:
            print(f'name = {ch.name} coord = {ch.show_coord()}')

child1 = Child('Вася1')
child2 = Child('Вася2')

bus = Bus()
bus.add_child(child1)
bus.add_child(child2)
bus.show_coord_by_passengers()

bus.change_coord(100)

bus.show_coord_by_passengers()



