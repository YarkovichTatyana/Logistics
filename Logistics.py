# 7. Разработайте программу, имитирующую работу транспортного агентства. Транспортное агентство имеет
# сеть филиалов в нескольких городах. Транспортировка грузов осуществляется между этими городами тремя
# видами транспорта: автомобильным, железнодорожным и воздушным. Любой вид транспортировки имеет стоимость
# единицы веса на единицу пути и скорость доставки. Воздушный транспорт можно использовать только между
# крупными городами, этот вид самый скоростной и самый дорогой.  Железнодорожный транспорт можно
# использовать между крупными и средними городами, этот вид самый дешевый. Автомобильный транспорт можно
# использовать между любыми городами. Заказчики через случайные промежутки времени обращаются в один
# из филиалов транспортного агентства с заказом на перевозку определенной массы груза и возможным пожеланием
# о скорости/цене доставки. Транспортное агентство организует отправку грузов одним из видов транспорта
# с учетом пожеланий клиента.
#
# -Доход транспортного агентства, в том числе с разбивкой по видам транспорта и городам.
# -Среднее время доставки груза, в том числе с разбивкой по видам транспорта и городам.
# -Список исполняемых заказов с возможностью сортировки по городам, видам транспорта, стоимости перевозки.
import random


class Transport_agency:
    list_of_branch = 'Minsk, Gomel, Brest, Grodno, Vitebsk,Mogilev, Moskow, Kiev'
    list_of_distans = {
        'Minsk_Gomel': 309, 'Gomel_Minsk': 309,  # 3.26 ~ время поездки
        'Minsk_Brest': 348, 'Brest_Minsk': 348,  # 3.49
        'Minsk_Grodno': 282, 'Grodno_Minsk': 282,  # 3.39
        'Minsk_Vitebsk': 294, 'Vitebsk_Minsk': 294,  # 3.14
        'Minsk_Mogilev': 199, 'Mogilev_Minsk': 199,  # 2.25
        'Minsk_Kiev': 573, 'Kiev_Minsk': 573,  # 6.46
        'Minsk_Moskow': 688, 'Moskow_Minsk': 688,  # 7.41
        'Gomel_Brest': 649, 'Brest_Gomel': 649,  # 6,47
        'Gomel_Grodno': 593, 'Grodno_Gomel': 593,  # 6,31
        'Gomel_Vitebsk': 330, 'Vitebsk_Gomel': 330,  # 4,21
        'Gomel_Mogilev': 175, 'Mogilev_Gomel': 175,  # 2.32
        'Gomel_Kiev': 263, 'Kiev_Gomel': 263,  # 4,4
        'Gomel_Moskow': 661, 'Moskow_Gomel': 661,  # 8,34
        'Brest_Grodno': 239, 'Grodno_Brest': 239,  # 3,14
        'Brest_Vitebsk': 627, 'Vitebsk_Brest': 627,  # 6,39
        'Brest_Mogilev': 529, 'Mogilev_Brest': 529,  # 5,35
        'Brest_Kiev': 577, 'Kiev_Brest': 577,  # 7,29
        'Brest_Moskow': 1051, 'Moskow_Brest': 1051,  # 11,26
        'Grodno_Vitebsk': 536, 'Vitebsk_Grodno': 536,  # 6,13
        'Grodno_Mogilev': 478, 'Mogilev_Grodno': 478,  # 5,15
        'Grodno_Kiev': 712, 'Kiev_Grodno': 712,  # 10
        'Grodno_Moskow': 992, 'Moskow_Grodno': 992,  # 11,28
        'Vitebsk_Mogilev': 162, 'Mogilev_Vitebsk': 162,  # 2.13
        'Vitebsk_Kiev': 596, 'Kiev_Vitebsk': 596,  # 8,46
        'Vitebsk_Moskow': 517, 'Moskow_Vitebsk': 517,  # 6,29
        'Mogilev_Kiev': 440, 'Kiev_Mogilev': 440,  # 6.52
        'Mogilev_Moskow': 587, 'Moskow_Mogilev': 587,  # 7.17
        'Kiev_Moskow': 891, 'Moskow_Kiev': 891}  # 11,47
    airport = 'Minsk, Moskow, Gomel,Kiev'

    def __init__(self, location):
        self.location = location

    def info_distanse(self):
        print(self.list_of_distans)


class Transport(Transport_agency):
    d_city = {}

    # ok#
    def __init__(self, location, model, load_capacity, speed, price_city, price_intercity):
        super().__init__(location)
        self.model = model
        self.load_capacity = load_capacity
        self.speed = speed
        self.price_city = price_city
        self.price_intercity = price_intercity
        self.add()

    # ok#
    def add(self):  # добавление транспорта в реестр парка агентства
        if self.model not in self.d_city.keys():
            self.d_city.update(
                {self.model: (self.location, self.load_capacity, self.speed, self.price_city, self.price_intercity)})
        else:
            print('Error! Transport with this name exists, please enter a different name')

    # ok#
    @classmethod
    def cost_calculation_city(self, model, time,
                              wight):  # расчет стоимости перевозки в городе с учетом того, что самолеты и поезда не используются
        return round(float(self.d_city[model][3] * wight / self.d_city[model][1]), 2) * time


    ##
    @classmethod
    def cost_calculation_intercity(self, model, leave_city, come_city, wight):  # расчет стоимости перевозки за городом
        return float(round(
            self.list_of_distans[leave_city + '_' + come_city] * float(self.d_city[model][4]) * float(wight) / float(
                self.d_city[model][1]), 2))

    @classmethod
    def del_transport(self, model):
        if model in self.d_city.keys():
            del self.d_city[model]
        else:
            print('Error! This car is not in the fleet')
##
    @classmethod
    def info_transport (self, model):
        return self.d_city[model]

    # @classmethod
    # def change_locayion(self, model, new_city):
    #     print(model, ':', self.d_city[model], ' -before')
    #     if new_city in self.list_of_branch:
    #         a = self.d_city[model].split()
    #         a[0] = new_city + ','
    #         a = ' '.join(a)
    #         self.d_city[model] = a
    #         print(model, ':', self.d_city[model], ' -after')

    @classmethod
    def info_in_city(self, city):
        print(f'Наличие транспорта в городе {city}:')
        for key, value in self.d_city.items():
            if city in self.d_city[key]:
                print(key, value)

    @classmethod
    def time_delivery_intercity(self, speed, leave_city, come_city):
        return round((self.list_of_distans[leave_city + '_' + come_city] / speed), 2)


class Auto_transport(Transport):

    def __init__(self, location, model, load_capacity, speed, price_city, price_intercity):
        super().__init__(location, model, load_capacity, speed, price_city, price_intercity)

    @classmethod
    def info_only_auto(self):
        print('Список только автотранпорта:')
        for key, value in self.d_city.items():
            if int(self.d_city[key].split(', ')[3]) != 0:
                print(key, value)


class Train_transport(Transport):
    def __init__(self, location, model, load_capacity, speed, price_city, price_intercity):
        super().__init__(location, model, load_capacity, speed, price_city, price_intercity)

    @classmethod
    def info_only_train(self):
        print('Список только поездов:')
        for key, value in self.d_city.items():
            if int(self.d_city[key].split(', ')[3]) == 0 and int(self.d_city[key].split(', ')[2]) < 250:
                print(key, value)


class Airplane_transport(Transport):
    def __init__(self, location, model, load_capacity, speed, price_city, price_intercity):
        super().__init__(location, model, load_capacity, speed, price_city, price_intercity)

    @classmethod
    def info_only_airplane(self):
        print('Список только самолетов:')
        for key, value in self.d_city.items():
            if int(self.d_city[key].split(', ')[3]) == 0 and int(self.d_city[key].split(', ')[2]) > 250:
                print(key, value)


car1 = Auto_transport('Minsk', 'Iveko', 2.5, 65, 25, 0.6)
car2 = Auto_transport('Minsk', 'Volvo', 20, 80, 60, 3.8)
car3 = Auto_transport('Brest', 'Man', 5, 90, 50, 1.2)
car4 = Auto_transport('Brest', 'Man', 6, 90, 50, 1.2)
car5 = Auto_transport('Grodno', 'Daf', 15, 90, 60, 1.9)
car6 = Auto_transport('Mogilev', 'MAЗ', 20, 90, 50, 1.7)
train1 = Train_transport('Grodno', 'GV-50/5', 250, 80, 0, 1778)
train2 = Train_transport('Minsk', 'GV-30/6', 180, 80, 0, 1224)
plane1 = Airplane_transport('Minsk', 'AN_225', 640, 800, 0, 136)
plane2 = Airplane_transport('Minsk', 'AN_316', 400, 800, 0, 125)
Auto_transport.info_in_city('Minsk')
Auto_transport.info_in_city('Brest')
print('Весь автопарк:')
print(Transport.d_city)

day = 1
stop_list = {}
groupage_cargo = {}
offer_list = {}
while day <= 5:
    try:
        for key in stop_list:
            if day == stop_list[key][1] + 1:
                Auto_transport.d_city.update({key: stop_list[key][0]})
                del stop_list[key]
                print(
                    f'транспорт {key} осуществил доставку, список занятых {stop_list} , список свободных {Auto_transport.d_city}')
        number_orders_day = random.randint(0, 3)
        print(number_orders_day, 'number_orders_day')
        for i in range(1, number_orders_day + 1):
            request = input(
                'enter the point of departure, destination(if there is), weight of the cargo, time  and price of the delivery')
            if len(request.split()) == 5:
                offer_list = {}
                print(request.split())
                leave_city = request.split()[0]
                destination = request.split()[1]
                wight = float(request.split()[2])
                cost = float(request.split()[4])
                time = float(request.split()[3])

                for model in Transport.d_city.keys():
                    speed = float(Transport.d_city[model][2])
                    if Transport.d_city[model][0] == leave_city and Transport.d_city[model][1] >= wight and \
                            Auto_transport.time_delivery_intercity(speed, leave_city, destination) <= time and \
                            Auto_transport.cost_calculation_intercity(model, leave_city, destination, wight) <= cost:
                        if Auto_transport.d_city[model][3] == 0 and wight <= Transport.d_city[model][1]:
                            print('groupage_cargopppppppppppppp', groupage_cargo)
                            if model in groupage_cargo:
                                if Transport.d_city[model][1] * 0.8 < wight + wight_all <= Transport.d_city[model][1]:
                                    print(
                                        f'Excellent! The cargo by transport {Transport.info_transport(model)} can be sent!')
                                    choice = int(input('You can put on hold. yes - 1, no -2:'))
                                    if choice==1:
                                        a = groupage_cargo[model]
                                        wight_all =0
                                        name = input('input your name1')
                                        a.append([name, leave_city, destination, wight])
                                        groupage_cargo[model] = a
                                        del groupage_cargo[model]
                                        print(f'Your choice {Transport.d_city[model]}of cargo will be sent')
                                        stop_list[model] = (Transport.d_city[model], day)
                                        Transport.del_transport(model)
                                elif Transport.d_city[model][1] * 0.8 > wight + wight_all:
                                    print("The order is too small")
                                    choice = int(input('You can put on hold. yes - 1, no -2:'))
                                    if choice == 1:
                                        a = groupage_cargo[model]
                                        wight_all += wight
                                        name = input('input your name2')
                                        groupage_cargo[model] = [a, [name, leave_city, destination, wight]]
                                        print('shipment has been added to the waiting list', groupage_cargo)
                                        print('groupage_cargovwwwwwwwwwwwww', groupage_cargo)
                                elif wight_all + wight > Transport.d_city[model][1]:
                                    print('cargo is too heavy to be added to this vehicle')
                                    print('restart your search')
                                    print('groupage_cargovuyuuuuuuuuuuuuuu', groupage_cargo)
                            elif model not in groupage_cargo:
                                if Transport.d_city[model][1] * 0.8 < wight <= Transport.d_city[model][1]:
                                    offer_list[model] = \
                                        {
                                            f'cost {Auto_transport.cost_calculation_intercity(model, leave_city, destination, wight)},'
                                            f'shipping speed  {Auto_transport.time_delivery_intercity(speed, leave_city, destination)},'
                                            f' weight {wight}'}
                                    print('offer_listvddddddddddddd', offer_list)
                                elif Transport.d_city[model][1] * 0.8 > wight:
                                    print("The order is too small")
                                    choice = int(input('You can put on hold. yes - 1, no -2:'))
                                    if choice == 1:
                                        wight_all = wight
                                        name = input('input your name3')
                                        groupage_cargo.update({model: [[name, leave_city, destination, wight]]})
                                        print('shipment has been added to the waiting list', groupage_cargo)
                                    print('groupage_cargovffffffffffffff', groupage_cargo)

                        else:
                            print(f'free suitable transport {model, Auto_transport.d_city[model]}')
                            offer_list[model] = {
                                f'cost {Auto_transport.cost_calculation_intercity(model, leave_city, destination, wight)},'
                                f'shipping speed  {Auto_transport.time_delivery_intercity(speed, leave_city, destination)},'
                                f' weight {wight}'}
                if offer_list != {}:
                    print(f'Offer_list:')
                    n = 1
                    for key, value in offer_list.items():
                        key = str(n) + ':' + key
                        print(key, value)
                        n += 1
                    # if key groupage_cargo.keys():
#доработать добавление писка сборных грузов, если там этот заказ есть

                    choice = int(input('make your choice (name), if nothing fits - press "0":'))
                    if choice == 0:
                        offer_list = {}
                    else:
                        n = 1
                        for key, value in offer_list.items():
                            if n == choice:
                                print(f'Your choice {key, value}of cargo will be sent')
                                stop_list[key] = (Transport.d_city[key], day)
                                Transport.del_transport(key)
                                break
                            n += 1
                else:
                    print('there is no free transport with the necessary requests')
            if len(request.split()) == 4:
                count = 0
                for key, value in Auto_transport.d_city.items():
                    leave_city = request.split()[0]
                    speed = round(Auto_transport.d_city[key][2], 2)
                    wight = float(request.split()[1])
                    cost = float(request.split()[3])
                    time = float(request.split()[2])
                    if Auto_transport.d_city[key][3] != 0 and Auto_transport.d_city[key][0] == leave_city and \
                            Auto_transport.d_city[key][1] >= wight and \
                            Auto_transport.cost_calculation_city(key, time, wight) <= cost:
                        print(f'free suitable transport {key, Auto_transport.d_city[key]}')
                        count += 1

# дописать авто в пути, и список предложений

                if count == 0:
                    print('there is no free transport with the necessary requests')
    except RuntimeError:
        print('dictionary changed size during iteration')
    day += 1
print('Work week is over')

# Minsk 1.8 3 500
# Minsk Moskow 1.8 6 500
# Minsk Moskow 600 6 5000000
# Minsk Kiev 1.8 6 500000
# Minsk Grodno 1.8 12 500000
# Moskow Minsk  545 6 500


