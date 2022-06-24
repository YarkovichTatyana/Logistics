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
# -Список исполняемых заказов с возможность сортировки по городам, видам транспорта, стоимости перевозки.


class Transport_agency:
    dist_Minsk_Gomel=dist_Gomel_Minsk=309 #3.26 ~ время поездки
    dist_Minsk_Brest = dist_Brest_Minsk = 348 #3.49
    dist_Minsk_Grodno = dist_Grodno_Minsk = 282 #3.39
    dist_Minsk_Vitebsk = dist_Vitebsk_Minsk = 294 #3.14
    dist_Minsk_Mogilev = dist_Mogilev_Minsk = 199 #2.25
    dist_Minsk_Kiev = dist_Kiev_Minsk = 573 #6.46
    dist_Minsk_Moskow = dist_Moskow_Minsk = 688 #7.41
    dist_Gomel_Brest = dist_Brest_Gomel = 649 #6,47
    dist_Gomel_Grodno = dist_Grodno_Gomel = 593 #6,31
    dist_Gomel_Vitebsk = dist_Vitebsk_Gomel = 330 #4,21
    dist_Gomel_Mogilev = dist_Mogilev_Gomel = 175 #2.32
    dist_Gomel_Kiev = dist_Kiev_Gomel = 263 #4,4
    dist_Gomel_Moskow = dist_Moskow_Gomel = 661 #8,34
    dist_Brest_Grodno = dist_Grodno_Brest = 239  # 3,14
    dist_Brest_Vitebsk = dist_Vitebsk_Brest = 627  # 6,39
    dist_Brest_Mogilev = dist_Mogilev_Brest = 529  # 5,35
    dist_Brest_Kiev = dist_Kiev_Brest = 577  # 7,29
    dist_Brest_Moskow = dist_Moskow_Brest = 1051  # 11,26
    dist_Grodno_Vitebsk = dist_Vitebsk_Grodno = 536 # 6,13
    dist_Grodno_Mogilev = dist_Mogilev_Grodno = 478  # 5,15
    dist_Grodno_Kiev = dist_Kiev_Grodno = 712  # 10
    dist_Grodno_Moskow = dist_Moskow_Grodno = 992  # 11,28
    dist_Vitebsk_Mogilev = dist_Mogilev_Vitebsk = 162  # 2.13
    dist_Vitebsk_Kiev = dist_Kiev_Vitebsk = 596  # 8,46
    dist_Vitebsk_Moskow = dist_Moskow_Vitebsk = 517  # 6,29
    dist_Mogilev_Kiev = dist_Kiev_Mogilev = 440  # 6.52
    dist_Mogilev_Moskow = dist_Moskow_Mogilev = 587  # 7.17
    dist_Kiev_Moskow = dist_Moskow_Kiev = 891 #11,47

    def __init__(self,location):
        self.location=location

class Transport(Transport_agency):
    def __init__(self, location, model, load_capacity, speed, price_city, price_intercity):
        super().__init__(location)
        self.model=model
        self.load_capacity=load_capacity
        self.speed=speed
        self.price_city = price_city
        self.price_intercity=price_intercity

class Auto_transport (Transport):
    d_Minsk = {}
    d_Brest = {}
    d_Grodno = {}
    d_Vitebsk = {}
    d_Mogilev = {}
    d_Gomel = {}
    d_Moskow = {}
    d_Minsk = {}
    d_city={}
    # self.city = city = {}
    def __init__(self, location, model, load_capacity, speed, price_city, price_intercity):
        super().__init__(location, model, load_capacity, speed, price_city, price_intercity)


    def add (self):
        self.d_city.update({self.model:{self.location, self.load_capacity,self.speed,self.price_city,self.price_intercity}})
    @classmethod
    def info_auto_city(self,city):
            print(f'Наличие авто в городе {city}:')
            for key,value in self.d_city.items():
                if city in self.d_city[key]:
                    print(key,value)
    @classmethod
    def info_auto_all(self):
            print('Автопарк агентства:')
            for key,value in self.d_city.items():
                    print(key,value)

    

#price_city - 1 hour
#price_intercity - 1 km
car1=Auto_transport('Minsk','Iveko',2.5,65,25,0.6)
car1.add()
car2=Auto_transport('Minsk','Volvo',20,80,60,3.8)
car2.add()
car3 =Auto_transport('Brest', 'Man',5,90,50,1.2)
car3.add()
Auto_transport.info_auto_city('Minsk')
Auto_transport.info_auto_city('Brest')
Auto_transport.info_auto_all()







