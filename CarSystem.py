'''In this file is all the logic for the project'''
from Cars import Car as car
from Clients import Client as person

Rent_cars = []
Vehicle = []
Human = []


def rent():
    count_cars = int(input("How many cars do you want to rent: "))
    client_name = input("Enter client name: ")
    for i in Human:
        if person.get_name(i) == client_name:
            if count_cars > 3:
                while count_cars > 0:
                    choose_car = input("enter the registration number of the car you want: ")
                    for j in Vehicle:
                        if car.get_regnum(j) == choose_car:
                            time = input("Choose between 'hours', a 'day' or a 'week': ")
                            if time == "hours":
                                rent_time = int(input("How many hours(enter number): "))
                                total_price = (car.get_pphour(j) * rent_time)
                            elif time == "day":
                                total_price = car.price_per_day()
                            elif time == "week":
                                total_price = car.price_per_week()
                            discount = discount + (total_price * 0.3)
                            rented = car.get_car(j), person.get_clients(i)
                            Rent_cars.append(rented)
                            Vehicle.remove(j)
                            count_cars = count_cars - 1
                    else:
                        print("no such car")
                Rent_cars.extend(discount)
            else:
                choose_car = input("enter the registration number of the car you want: ")
                for j in Vehicle:
                    if car.get_regnum(j) == choose_car:
                        time = input("Choose between 'hours', a 'day' or a 'week': ")
                        if time == "hours":
                            rent_time = int(input("How many hours(enter number): "))
                            total_price = (car.get_pphour(j) * rent_time)
                        elif time == "day":
                            total_price = car.price_per_day()
                        elif time == "week":
                            total_price = car.price_per_week()
                        rented = car.get_car(j), person.get_clients(i), total_price
                        Rent_cars.append(rented)
                        Vehicle.remove(j)


def add_car():
    car_brand = input("Enter car brand: ")
    car_model = input("Enter car model: ")
    car_cost = input("Enter car cost: ")
    car_regnum = input("Enter car registration number: ")
    car_pph = int(input("Enter price per hour: "))
    enter_car = car(car_brand, car_model, car_cost, car_regnum, car_pph)
    Vehicle.append(enter_car)


def add_client():
    client_name = input("Enter client name: ")
    client_age = input("Enter client age: ")
    client_id = int(input("Enter client id: "))
    enter_person = person(client_name, client_age, client_id)
    Human.append(enter_person)


def list_cars():
    for i in Vehicle:
        car.print_car(i)


def list_rented():
    for i in Rent_cars:
        print(i)


if __name__ == "__main__":
    print("if you want to add new client write 'add client'\n"
          "if you want to add new car write 'add car'\n"
          "if you want to rent a car write 'rent'\n"
          "if you want to list all rented cars  write 'rent'\n"
          "if you want to list all available cars for rent write 'list'\n")
    commands = ""
    while commands != "exit":
        commands = input("Choose your option: ")
        if commands == "add client":
            add_client()
        elif commands == "add car":
            add_car()
        elif commands == "rent":
            rent()
        elif commands == "list":
            list_cars()
        elif commands == "list rented":
            list_rented()
        elif commands == "exit":
            break
    else:
        print("Wrong option, Try again")
