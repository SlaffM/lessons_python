class Homan():



    def __init__(self, v_name):
        self.__head = 1
        self.__hands = 2
        self.__name = v_name

    def __str__(self):
        return f'name = {self.get_name()}'

    def get_name(self):
        return self.__name


class Child(Homan):

    def __init__(self, v_name):
        super().__init__(v_name)
        self.__coord = 0

    def set_coord(self, v_coord):
        self.__coord = v_coord

    def get_coord(self):
        return(self.__coord)

class Bus():

    def __init__(self):
        self.__l1 = list()

    def add_child(self, ch: Child):
        self.__l1.append(ch)

    def del_child(self, ch: Child):
        self.__l1.remove(ch)

    def set_coord(self, v_coord):
        for ch in self.__l1:
            ch.set_coord(v_coord)

    def get_passangers(self):
        for ch in self.__l1:
            print(ch)

    def get_coord_by_passengers(self):
        for ch in self.__l1:
            print(f'name = {ch.get_name()} coord = {ch.get_coord()}')


child1 = Child('Вася1')
child2 = Child('Вася2')

bus = Bus()
bus.add_child(child1)
bus.add_child(child2)
bus.get_coord_by_passengers()

bus.set_coord(100)

bus.get_coord_by_passengers()
print('--------------------------')
bus.del_child(child1)
bus.get_coord_by_passengers()