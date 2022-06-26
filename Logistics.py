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
        'Minsk_Gomel': 309,  # 3.26 ~ время поездки
        'Minsk_Brest': 348,  # 3.49
        'Minsk_Grodno': 282,  # 3.39
        'Minsk_Vitebsk': 294,  # 3.14
        'Minsk_Mogilev': 199,  # 2.25
        'Minsk_Kiev': 573,  # 6.46
        'Minsk_Moskow': 688,  # 7.41
        'Gomel_Brest': 649,  # 6,47
        'Gomel_Grodno': 593,  # 6,31
        'Gomel_Vitebsk': 330,  # 4,21
        'Gomel_Mogilev': 175,  # 2.32
        'Gomel_Kiev': 263,  # 4,4
        'Gomel_Moskow': 661,  # 8,34
        'Brest_Grodno': 239,  # 3,14
        'Brest_Vitebsk': 627,  # 6,39
        'Brest_Mogilev': 529,  # 5,35
        'Brest_Kiev': 577,  # 7,29
        'Brest_Moskow': 1051,  # 11,26
        'Grodno_Vitebsk': 536,  # 6,13
        'Grodno_Mogilev': 478,  # 5,15
        'Grodno_Kiev': 712,  # 10
        'Grodno_Moskow': 992,  # 11,28
        'Vitebsk_Mogilev': 162,  # 2.13
        'Vitebsk_Kiev': 596,  # 8,46
        'Vitebsk_Moskow': 517,  # 6,29
        'Mogilev_Kiev': 440,  # 6.52
        'Mogilev_Moskow': 587,  # 7.17
        'Kiev_Moskow': 891}  # 11,47
    airport = 'Minsk, Moskow, Gomel,Kiev'

    def __init__(self, location):
        self.location = location

    def info_distanse(self):
        print(self.list_of_distans)


class Transport(Transport_agency):
    d_city = {}
#ok#
    def __init__(self, location, model, load_capacity, speed, price_city, price_intercity):
        super().__init__(location)
        self.model = model
        self.load_capacity = load_capacity
        self.speed = speed
        self.price_city = price_city
        self.price_intercity = price_intercity
        self.add()
#ok#
    def add(self):  # добавление транспорта в реестр парка агентства
        if self.model not in self.d_city.keys():
            self.d_city.update(
                {self.model: (self.location, self.load_capacity, self.speed, self.price_city, self.price_intercity)})
        else:
            print('Error! Transport with this name exists, please enter a different name')

    #ok#
    @classmethod
    def cost_calculation_city(self, model, time,
                              wight):  # расчет стоимости перевозки в городе с учетом того, что самолеты и поезда не используются
        return round(float(self.d_city[model][3] * wight / self.d_city[model][1]), 2) * time
        # else:
        #     return'This type of transport is not used for delivery within the city'

    ##
    @classmethod
    def cost_calculation_intercity(self, model, leave_city, come_city, wight):  # расчет стоимости перевозки за городом
        if self.d_city[model][3] != 0:
            if leave_city in self.airport and come_city in self.airport:
                return round(self.list_of_distans[leave_city + '_' + come_city] * float(
                    self.d_city[model][4]) * float(wight) / float(self.d_city[model][1]), 2)
        else:
            return round(
                self.list_of_distans[leave_city + '_' + come_city] * float(self.d_city[model][4]) * float(
                    wight) / float(self.d_city[model][1]), 2)

    @classmethod
    def del_transport(self, model):
        if model in self.d_city.keys():
            del self.d_city[model]
        else:
            print('Error! This car is not in the fleet')

    @classmethod
    def info_type_all(self):
        self.info_all = self.d_city
        # print('Парк транcпорта агентства ')
        # for key,value in self.d_city.items():
        #     print(key,value)

    @classmethod
    def change_locayion(self, model, new_city):
        print(model, ':', self.d_city[model], ' -before')
        if new_city in self.list_of_branch:
            a = self.d_city[model].split()
            a[0] = new_city + ','
            a = ' '.join(a)
            self.d_city[model] = a
            print(model, ':', self.d_city[model], ' -after')

    @classmethod
    def info_in_city(self, city):
        print(f'Наличие транспорта в городе {city}:')
        for key, value in self.d_city.items():
            if city in self.d_city[key]:
                print(key, value)

    ##
    @classmethod
    def time_delivery_intercity(self, speed, leave_city, come_city):
        return round((self.list_of_distans[leave_city + '_' + come_city] / speed), 2)
        # print(time)


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
Auto_transport.info_in_city('Minsk')
Auto_transport.info_in_city('Brest')
Auto_transport.info_type_all()
# Auto_transport.change_locayion('Iveko', 'Vitebsk')

# Auto_transport.cost_calculation_intercity('Man','Minsk','Kiev',4)
print(Auto_transport.list_of_distans)
Auto_transport.del_transport('Man')
Auto_transport.info_type_all()
car4 = Auto_transport('Brest', 'Man', 6, 90, 50, 1.2)
Auto_transport.info_type_all()
train1 = Train_transport('Grodno', 'GV-50/5', 250, 80, 0, 1778)
train2 = Train_transport('Minsk', 'GV-30/6', 180, 80, 0, 1224)
Train_transport.info_type_all()
print(Train_transport.d_city)
# Auto_transport.info_only_auto()
# Train_transport.info_only_train()
plane1 = Airplane_transport('Minsk', 'AN_225', 640, 800, 0, 136)
# Airplane_transport.info_only_airplane()
print(Train_transport.d_city)
# Airplane_transport.cost_calculation_intercity('AN_225','Minsk','Moskow',135)


#
day = 1
groupage_cargo={}
while day <= 7:
    number_orders_day = random.randint(0, 4)
    for i in range(0, number_orders_day + 1):
        request = input(
            'enter the point of departure, destination(if there is), weight of the cargo, time  and price of the delivery')
        print(request.split( ))
        if len(request.split( ))==5:
            count=0
            for key in Auto_transport.d_city:
                leave_city=request.split()[0]
                speed = Auto_transport.d_city[key][2]
                destination = request.split()[1]
                wight = request.split()[2]
                cost = request.split()[4]

                if Auto_transport.d_city[key][0]==leave_city and float(Auto_transport.d_city[key][1])>=float(request.split( )[2]) and\
                        Auto_transport.time_delivery_intercity(speed,leave_city, destination)<=float(request.split( )[3])and\
                        float(Auto_transport.cost_calculation_intercity(key,leave_city,destination,wight))<=float(cost):
                    if Auto_transport.d_city[key][3] == 0 and float(wight) <(Auto_transport.d_city[key][1])*0.8:
                        print('need to wait for cargo')
                        m=int(input("you need to choose: 1 - I'm waiting for a groupage cargo 2 - I need another option:"))
                        if m==1:
                            name=input('input your name')
                            if key in groupage_cargo:
                                summa_wight=0
                                groupage_cargo[key].update({name:float(wight)})
                                key_model=key
                                if key_model in groupage_cargo:
                                    for key_name in key_model[key]:
                                        summa_wight+=key_model[key]
                                        print('summa_wight=',summa_wight)
                                        if summa_wight>Auto_transport.d_city[key_model][1]:
                                            print('cargo is too heavy to be added to this vehicle')
                                            print('restart your search')
                                        elif (Auto_transport.d_city[key_model][1])*0.8<=summa_wight<=Auto_transport.d_city[key_model][1]:
                                            print(f'Excellent! The cargo {key_model[key]} can be sent!')
                            else:
                                groupage_cargo.update({key:{name:float(wight)}})
                            print('shipment has been added to the waiting list', groupage_cargo)
                    elif Auto_transport.d_city[key][3] == 0 and key in groupage_cargo:
                        name=input('input your name')
                        summa_wight = 0
                        groupage_cargo[key].update({name: float(wight)})
                        for key_name in groupage_cargo[key]:
                            summa_wight += groupage_cargo[key][key_name]
                            print('summa_wight=', summa_wight)
                            if summa_wight > Auto_transport.d_city[key][1]:
                                print('cargo is too heavy to be added to this vehicle')
                                print('restart your search')
                            elif (Auto_transport.d_city[key][1]) * 0.8 <= summa_wight <= Auto_transport.d_city[key][1]:
                                print(f'Excellent! The cargo {key,groupage_cargo[key]} can be sent!')

                    else:
                        print(f'free suitable transport {key,Auto_transport.d_city[key]}')
                        count+=1
            if count==0:
                print('there is no free transport with the necessary requests')

        # if len(request.split()) == 4:
        #     count = 0
        #     for key, value in Auto_transport.d_city.items():
        #         leave_city = request.split()[0]
        #         speed = round(Auto_transport.d_city[key][2], 2)
        #         wight = float(request.split()[1])
        #         cost = float(request.split()[3])
        #         time = float(request.split()[2])
        #         if Auto_transport.d_city[key][3] != 0 and Auto_transport.d_city[key][0] == leave_city and \
        #                 Auto_transport.d_city[key][1] >= wight and \
        #                 Auto_transport.cost_calculation_city(key, time, wight) <= cost:
        #             print(f'free suitable transport {key, Auto_transport.d_city[key]}')
        #             count += 1
        #
        #     if count == 0:
        #         print('there is no free transport with the necessary requests')

# Minsk 1.8 3 500
# Minsk Moskow 1.8 6 500
#Minsk Moskow 600 6 5000000
# Minsk Kiev 1.8 6 500000*
# Minsk Grodno 1.8 12 500000


# price_city - 1 hour
# price_intercity - 1 km
