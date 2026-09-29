routes = {
    "1": ("Москва", "Сочи", 10000),
    "2": ("Москва", "Санкт-Петербург", 3500),
    "3": ("Москва", "Казань", 4200),
    "4": ("Москва", "Екатеринбург", 5800),
    "5": ("Москва", "Новосибирск", 7400),
    "6": ("Москва", "Калининград", 6900),
    "7": ("Москва", "Мурманск", 8300),
    "8": ("Москва", "Владивосток", 15600),
    "9": ("Санкт-Петербург", "Сочи", 9200),
    "10": ("Казань", "Сочи", 7800),
    "11": ("Екатеринбург", "Санкт-Петербург", 6100),
}


def op():
    print(" ")
    print("АВИАСЕЙЛС")
    print("1: купить билеты")
    print("2: отели")
    print("0: выход")


def menu():
    print(" ")
    print("билеты")
    print("1: выбор маршрута")


def menu_bilet():
    print(" ")
    print("- - - - - - купить билеты - - - - - -")
    print("на АВИАСЕЙЛС\n")
    print("0: назад")
    for key, (frm, to, price) in routes.items():
        print(f"{key}: {frm} - {to} {price:,}₽".replace(",", " "))
    print()


def buy_ticket():
    while True:
        menu_bilet()
        choice = input("Выберите маршрут: ")

        if choice == "0":
            return
        elif choice in routes:
            frm, to, price = routes[choice]
            print(f"\nВы выбрали: {frm} - {to} за {price:,}₽".replace(",", " "))
            input("Нажмите Enter, чтобы продолжить...")
            return
        else:
            print("Неверный пункт, попробуйте снова")


def main():
    print("mini авиасейлс")
    print("добро пожаловать на авиасейлс")

    while True:
        op()
        a = input("Выберите пункт: ")

        if a == "0":
            print("Выход...")
            break
        elif a == "1":
            menu()
            b = input("Выберите пункт меню: ")
            if b == "1":
                buy_ticket()
        elif a == "2":
            print("\nОтели скоро появятся ")
        else:
            print("Неверный пункт, попробуйте снова")


if __name__ == "__main__":
    main(