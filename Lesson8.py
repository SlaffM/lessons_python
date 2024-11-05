class Human():
    __name: str
    __age: int

    def __init__(self, v_name: str, v_age : int):
        self.__name = v_name
        self.__age = v_age

    def get_info(self):
        return f'human: name = {self.__name} age = {self.__age}'

    def get_name(self):
        return self.__name

    def __str__(self):
        return self.get_info()


class RotaOther():

    __title: str

    def __init__(self, v_title):
        self.__title = v_title

    def get_info(self):
        return self.__title

class Rota():

    __humans: list()

    def __init__(self, title='rota'):
        self.__humans = list()
        self.__title = title

    def add_humans(self, v_humans: list()):
        try:
            self.__humans += v_humans
        except Exception as e:
            print(f'Ошибка добавления человека в Роту', e)

    def del_humans(self, v_humans: list()):
        for h in v_humans:
            for hl in self.__humans:
                if hl.get_name() == h.get_name():
                    self.__humans.remove(hl)

    def get_info(self):
        print(f' title = {self.__title}')
        for hl in self.__humans:
            print(f'  {hl.get_info()}')

    def get_title(self):
        return self.__title

    def get_humans(self):
        return self.__humans

    def __str__(self):
        return self.get_info()

class Polk():

    def __init__(self, title='polk'):
        self.__rots = list()
        self.__title = title

    def get_rots(self):
        return self.__rots

    def add_rota(self, v_rota: Rota):
        self.__rots.append(v_rota)

    def del_humans(self, v_humans: list()):
        for r in self.__rots:
            try:
                r.del_humans(v_humans)
            except Exception as e:
                print(e)

    def get_info(self):
        print(f' title = {self.__title}')
        for r in self.__rots:
            try:
                print(f'  title = {r.get_title()}')
                for hl in r.get_humans():
                        print(f'   {hl.get_info()}')
            except Exception as e:
                print(r, e)

    def get_title(self):
        return self.__title

def Main():

    list_humans = list()
    for i1 in range(10):
        list_humans.append(Human('h'+str(i1), 18 + i1))

    for h1 in list_humans:
        print(h1.get_info())

    list_humans2 = list()
    for i2 in range(10,20,1):
        list_humans2.append(Human('h'+str(i2), 18 + i2))

    for h2 in list_humans2:
        print(h2.get_info())

    print('___________________________')

    r1 = Rota('r1')
    try:
        r1.add_humans(list_humans)
        #r1.add_humans([h5])
        print(f'-added humans to rota1')
        r1.get_info()
        print(f'-delete humans h2 from rota1')
        h6 = Human('h6', 20)
        r1.del_humans(h6)
        r1.get_info()
    except Exception as e:
        print(e)

    print(f'-added humans to rota2')
    r2 = Rota('r2')
    r2.add_humans(list_humans2)
    r2.get_info()
    print('___________________________')

    rOther = RotaOther('Другая Рота')
    p1 = Polk('p1')
    p1.add_rota(r1)
    p1.add_rota(r2)

    try:
        p1.add_rota(rOther)
    except Exception as e:
        print(e)

    print('_added r1, r2 to polk')
    p1.get_info()
    print('-delete human h5 from polk')
    h15 = Human('h15', 33)
    p1.del_humans([h15])
    p1.get_info()

Main()






