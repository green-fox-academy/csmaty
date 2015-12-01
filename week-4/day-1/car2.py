class Car:
    def __init__(self, color, cartype, km):

        if type(color) != str:
            raise exception ('color is not a string')

        self.color = color
        self.cartype = cartype
        self.km = km

    def ride(self, km):
        self.km += km

    def getMiles(self):
        return self.km * 0.6213

tesla = Car('pink', 'Tesla S', 1200)

tesla.ride(220)

lada = Car('red', 'Lada 1200', 1200)


print(tesla.km)
print(tesla.getMiles())
