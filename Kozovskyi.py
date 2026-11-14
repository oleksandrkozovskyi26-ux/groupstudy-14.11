from Chumachenko import Station
from Kravchenko import Electric_bike, Regular_bike
from Sulymenko import Client
from Bachurin import RentalService
def main():
    stations = {}
    bikes = {}
    clients = {}
    while True:
        try:
            com = input("add_stan - додати станцію\n"
                        "add_bike - додати велосипед\n"
                        "add_client - додати користувача\n"
                        "add_ride - додати поїздку\n"
                        "stop - зупинити програму\n"
                        "Введіть команду:  ")
            if com == "add_stan":
                name = input("Введіть назву станції: ")
                stations[name] = Station(name)
            elif com == "add_bike":
                    command = input("number - номер велосипеда\n"
                                    "type - тип(reg - звичайний, elec - електричний)\n"
                                    "station - назва станції розташування\n"
                                    "Введіть у форматі \"number type station\": ").split(" ")
                    if command[1] == "reg":
                        bikes[command[0]] = Regular_bike(command[0])
                        stations[command[2]].add_bike(bikes[command[0]])
                    elif command[1] == "elec":
                        bikes[command[0]] = Electric_bike(command[0])
                        stations[command[2]].add_bike(bikes[command[0]])
            elif com == "add_client":
                command = input("name - ім'я клієнта\n"
                      "balance - баланс\n"
                      "Введіть у форматі \"name balance\": ").split(" ")
                clients[command[0]] = Client(command[0], float(command[1]))
            elif com == "add_ride":
                command = input("name - ім'я клієнта\n"
                                "time - час поїздки\n"
                                "number - номер велосипеда\n"
                                "station1 - назва станції початкового розташування\n"
                                "station2 - назва станції кінцевого розташування\n"
                                "Введіть у форматі \"name time number station1 station2\": ").split(" ")
                cost =  bikes[command[2]].rent(command[1])
                if clients[command[0]].deduct_money(cost):
                    print("Поїздка завершена")
                else:
                    raise ValueError
                stations[command[4]].add_bike(command[2])
                stations[command[3]].remove_bike(command[2])
            elif com == "stop":
                break
        except:
            print("Помилковий ввід")
            continue


main()