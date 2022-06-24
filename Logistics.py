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


class Transport_agency:
    list_of_branch='Minsk, Gomel, Brest, Grodno, Vitebsk,Mogilev, Moskow, Kiev'
    list_of_distans={
        'Minsk_Gomel': 309, #3.26 ~ время поездки
        'Minsk_Brest' : 348, #3.49
        'Minsk_Grodno' : 282, #3.39
        'Minsk_Vitebsk' : 294, #3.14
        'Minsk_Mogilev' : 199, #2.25
        'Minsk_Kiev':573, #6.46
        'Minsk_Moskow' : 688, #7.41
        'Gomel_Brest' : 649, #6,47
        'Gomel_Grodno' : 593, #6,31
        'Gomel_Vitebsk' : 330, #4,21
        'Gomel_Mogilev' :175, #2.32
        'Gomel_Kiev' : 263, #4,4
        'Gomel_Moskow' : 661, #8,34
        'Brest_Grodno': 239,  # 3,14
        'Brest_Vitebsk' : 627,  # 6,39
        'Brest_Mogilev' : 529,  # 5,35
        'Brest_Kiev' : 577,  # 7,29
        'Brest_Moskow' :1051, # 11,26
        'Grodno_Vitebsk': 536,# 6,13
        'Grodno_Mogilev': 478, # 5,15
        'Grodno_Kiev' :712 , # 10
        'Grodno_Moskow' : 992 , # 11,28
        'Vitebsk_Mogilev' : 162 , # 2.13
        'Vitebsk_Kiev' : 596 , # 8,46
        'Vitebsk_Moskow' : 517 , # 6,29
        'Mogilev_Kiev' : 440 , # 6.52
        'Mogilev_Moskow' : 587 , # 7.17
        'Kiev_Moskow' : 891 }#11,47


    def __init__(self,location):
        self.location=location
    def info_distanse(self):
        print(self.list_of_distans)

class Transport(Transport_agency):
    d_city={}
    def __init__(self, location, model, load_capacity, speed, price_city, price_intercity):
        super().__init__(location)
        self.model=model
        self.load_capacity=load_capacity
        self.speed=speed
        self.price_city = price_city
        self.price_intercity=price_intercity
        self.add()

    def add (self): #добавление транспорта в реестр парка агентства
        if self.model not in self.d_city.keys():
            self.d_city.update({self.model:f'{self.location}, {self.load_capacity}, {self.speed}, {self.price_city}, {self.price_intercity}'})
        else:
            print('Error! Transport with this name exists, please enter a different name')

    @classmethod
    def cost_calculation_city (self,model,time,wight):#расчет стоимости перевозки в городе с учетом того, что самолеты и поезда не используются
        if self.d_city[model][3]!=0:
            print(f'стоимость перевозки за {time} часа транспортом {model} груза {wight} тонн равна {round(time*float(self.d_city[model].split(", ")[3])*wight/float(self.d_city[model].split(", ")[1]),2)} рублей')
        else:
            print('This type of transport is not used for delivery within the city')
    @classmethod
    def cost_calculation_intercity (self,model,leave_city, come_city,wight):#расчет стоимости перевозки за городом
        route=leave_city+'_'+come_city
        print('route=', route)
        if route in self.list_of_distans.keys():
            print(f'стоимость перевозки за  расстояние {self.list_of_distans[route]} км транспортом {model} равна {round(self.list_of_distans[route]*float(self.d_city[model].split(", ")[4])*wight/float(self.d_city[model].split(", ")[1]),2)}')
        else:
            print('There is no such direction')

    @classmethod
    def del_transport (self,model):
        if model in self.d_city.keys():
            del self.d_city[model]
        else:
            print('Error! This car is not in the fleet')

    @classmethod
    def info_type_all(self):
        print('Парк транcпорта агентства ')
        for key,value in self.d_city.items():
            print(key,value)
    @classmethod
    def change_locayion(self, model, new_city):
        print(model,':', self.d_city[model],' -before')
        if new_city in self.list_of_branch:
            a=self.d_city[model].split()
            a[0]=new_city+','
            a=' '.join(a)
            self.d_city[model]=a
            print(model,':',self.d_city[model],' -after')

    @classmethod
    def info_in_city(self,city):
        print(f'Наличие транспорта в городе {city}:')
        for key,value in self.d_city.items():
            if city in self.d_city[key]:
                print(key,value)

class Auto_transport (Transport):

    def __init__(self, location, model, load_capacity, speed, price_city, price_intercity):
        super().__init__(location, model, load_capacity, speed, price_city, price_intercity)

    @classmethod
    def info_only_auto(self):
        print('Список только автотранпорта:')
        for key,value in self.d_city.items():
            if int(self.d_city[key].split(', ')[3])!=0:
                print(key,value)


class Train_transport (Transport):
    def __init__(self, location, model, load_capacity, speed, price_city, price_intercity):
        super().__init__(location, model, load_capacity, speed, price_city, price_intercity)

    @classmethod
    def info_only_train(self):
        print('Список только поездов:')
        for key,value in self.d_city.items():
            if int(self.d_city[key].split(', ')[3])==0 and int(self.d_city[key].split(', ')[2])<250:
                print(key,value)

class Airplane_transport (Transport):
    def __init__(self, location, model, load_capacity, speed, price_city, price_intercity):
        super().__init__(location, model, load_capacity, speed, price_city, price_intercity)

    @classmethod
    def info_only_airplane(self):
        print('Список только самолетов:')
        for key,value in self.d_city.items():
            if int(self.d_city[key].split(', ')[3])==0 and int(self.d_city[key].split(', ')[2])>250:
                print(key,value)
# day=1
# while day<=7:
#





#price_city - 1 hour
#price_intercity - 1 km
car1=Auto_transport('Minsk','Iveko',2.5,65,25,0.6)
car2=Auto_transport('Minsk','Volvo',20,80,60,3.8)
car3 =Auto_transport('Brest', 'Man',5,90,50,1.2)
Auto_transport.info_in_city('Minsk')
Auto_transport.info_in_city('Brest')
Auto_transport.info_type_all()
Auto_transport.change_locayion('Iveko', 'Vitebsk')
Auto_transport.cost_calculation_city('Iveko',3.25,2)
Auto_transport.cost_calculation_intercity('Man','Minsk','Kiev',4)
print(Auto_transport.list_of_distans)
Auto_transport.del_transport('Man')
Auto_transport.info_type_all()
car4 =Auto_transport('Brest', 'Man',6,90,50,1.2)
Auto_transport.info_type_all()
train1=Train_transport('Grodno','GV-50/5',250, 80,0, 1778)
train2=Train_transport('Minsk','GV-30/6',180, 80,0, 1224)
Train_transport.info_type_all()
print(Train_transport.d_city)
Auto_transport.info_only_auto()
Train_transport.info_only_train()
plane1=Airplane_transport('Minsk','AN_225',640, 800, 0, 136)
Airplane_transport.info_only_airplane()
print(Train_transport.d_city)
Airplane_transport.cost_calculation_intercity('AN_225','Minsk','Moskow',135)





