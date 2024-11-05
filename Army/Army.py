import datetime as dt

class Human():
    __name: str
    __age: int
    __birthday: dt

    def __init__(self, v_name: str, v_age : int):
        self.__name = v_name
        self.__age = v_age
        self.__get_birthday(v_age)

    def get_info(self):
        return f'human: name = {self.__name} age = {self.__age} birth = {self.__birthday}'

    def get_name(self):
        return self.__name

    def __str__(self):
        return self.get_info()

    def __get_birthday(self, v_age):
        today = dt.date.today()
        #print(f'today = {today}')
        birth = dt.date(year=today.year-self.__age, month=1, day=10)
        #print(f'birth = {birth}')
        self.__birthday = birth

        #print(dt.date.strftime(self.__birthday, '%c'))
        return self.__birthday




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