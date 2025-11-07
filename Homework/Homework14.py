# N1 - N2
# შექმენით პითონის კლასი Car, ატრიბუტებით: ბრენდი, მოდელი და წელი. 
# ასევე, შექმენით კლასის მეთოდი car_info(), 
# რომელიც დაბეჭდავს ატრიბუტების ინფორმაციას.

# Car კლასში დაამატეთ მეთოდი age_of_car, რომელიც დაითვლის მანქანის ასაკს. 
# ავტომობილის ასაკი დაბეჭდეთ car_info() მეთოდიდან.

# N4
# დაამატეთ Car კლასს ატრიბუტი number_of_cars, 
# რომელიც დაითვლის მანქანების სრულ რაოდენობას. 
# გაზარდეთ ეს ცვლადი ყოველ ჯერზე, მანქანის შექმნისას. 

# N5
# Car კლასს დაამატეთ მეთოდი total_cars(), 
# რომელიც გამოიტანს მანქანების მთლიან რაოდენობას.

class Car():
    number_of_cars = 0

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        
        Car.number_of_cars += 1
        
    def age_of_car(self):
        return 2025 - self.year

    def total_cars(self):
        print(f"მანქანების რაოდენობა: {Car.number_of_cars}")

    def car_info(self):
        print(f"ბრენდი: {self.brand}, მოდელი: {self.model}, წელი: {self.year}, ასაკი: {self.age_of_car()}")

toyota = Car("Toyota", "Camry", 2020)
toyota.car_info()



class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_life):
        super().__init__(brand, model, year)
        self.battery_life = battery_life

    def battery_info(self):
        print(f"ამ მანქანის ბატარეის ხანგრძლივობა არის {self.battery_life} საათი")

tesla = ElectricCar("Tesla", "X", 2024, 50)
tesla.car_info()
tesla.battery_info()
tesla.total_cars()