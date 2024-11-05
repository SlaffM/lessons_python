import datetime as date
import time

import Army.Army as army



def Main():

    list_humans = list()
    for i1 in range(10):
        list_humans.append(army.Human('h'+str(i1), 18 + i1))

    for h1 in list_humans:
        print(h1.get_info())

    list_humans2 = list()
    for i2 in range(10,20,1):
        list_humans2.append(army.Human('h'+str(i2), 18 + i2))

    for h2 in list_humans2:
        print(h2.get_info())

    print('___________________________')

    r1 = army.Rota('r1')
    try:
        r1.add_humans(list_humans)
        #r1.add_humans([h5])
        print(f'-added humans to rota1')
        r1.get_info()
        print(f'-delete humans h2 from rota1')
        h6 = army.Human('h6', 20)
        r1.del_humans(h6)
        r1.get_info()
    except Exception as e:
        print(e)

    print(f'-added humans to rota2')
    r2 = army.Rota('r2')
    r2.add_humans(list_humans2)
    r2.get_info()
    print('___________________________')

    rOther = army.RotaOther('Другая Рота')
    p1 = army.Polk('p1')
    p1.add_rota(r1)
    p1.add_rota(r2)

    try:
        p1.add_rota(rOther)
    except Exception as e:
        print(e)

    print('_added r1, r2 to polk')
    p1.get_info()
    print('-delete human h5 from polk')
    h15 = army.Human('h15', 33)
    p1.del_humans([h15])
    p1.get_info()

Main()


