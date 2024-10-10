class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        for i in range(1, int(new_floor + 1)):
            if new_floor > self.number_of_floors or new_floor == 0:
                print('Такого этажа не существует')
                break
            else:
                print(i)

    def __len__(self):
        return int(self.number_of_floors)

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}.'


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
#  Название: ЖК Эльбрус, количество этажей: 10.
# Название: ЖК Акация, количество этажей: 20.
# 10
# 20
