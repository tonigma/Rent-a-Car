class Car:
    ''' PPHours is short form for - Price Per hour '''

    def __init__(self, brand, model, cost, regnum, pphour):
        self.Brand = brand
        self.Model = model
        self.Cost = cost
        self.RegNum = regnum
        self.PPHour = pphour

    def price_per_day(self):
        price_day = self.PPHour * 24
        return price_day

    def price_per_week(self):
        price_week = self.PPHour * 168
        return price_week

    def get_regnum(self):
        return self.RegNum

    def print_car(self):
        print("Car Brand: ", self.Brand, "Car Model: ", self.Model, "Car Cost: ", self.Cost,
              "Car Registration Number: ", self.RegNum, "Car Price Per Hour: ", self.PPHour)

    def get_car(self):
        return self.Brand, self.Model, self.Cost, self.RegNum

    def get_pphour(self):
        return self.PPHour
