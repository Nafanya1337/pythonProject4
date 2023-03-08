import random
import sys

import graphviz as graphviz


def generate_groups():
    groups = {
        'ИВБО': ["ИВБО-{:02d}-21".format(i) for i in range(1, 9)],
        'ИКБО': ["ИКБО-{:02d}-21".format(i) for i in range(1, 34) if i != 23 if i != 29],
        'ИМБО': ["ИМБО-{:02d}-21".format(i) for i in range(1, 3)],
        'ИНБО': ["ИНБО-{:02d}-21".format(i) for i in range(1, 14)]
    }
    return groups

def groups():
    groups = generate_groups()
    for a in groups:
        print(a)
        for i in range(0, len(groups[a])):
            if i % 10 == 0 and i != 0:
                print()
            print(groups[a][i], end=' ')
        print()

def myprint(a):
    sys.stdout.write (str(a) + '\n')

table = [
    ["Коллеги,", "В то же время,", "Однако,", "Тем не менее,", "Следовательно,", "Соответственно,", "Вместе с тем,",
     "С другой стороны,"],
    ["парадигма цифровой экономики", "контекст цифровой трансформации", "диджитализация бизнес-процессов",
     "прагматичный подход к цифровым платформам",
     "совокупность сквозных технологий", "программа прорывных исследований", "ускорение блокчейн-транзакций",
     "экспоненциальный рост Big Data"],
    ["открывает новые возможности для", "выдвигает новые требования", "несёт в себе риски", "расширяет горизонты",
     "заставляет искать варианты", "не оставляет шанса для", "повышает вероятность", "обостряет проблему", ],
    ["дальнейшего углубления", "бюджетного финансирования", "синергетического эффекта",
     "компрометации конфиденциальных", "универсальной коммодитизации", "несанкционированной кастомизации",
     "нормативного регулирования", " практического применения"],
    ["знаний и компетенций.", "непроверенных гипотез.", "волатильных активов.", "опасных экспериментов.",
     "сударственно-частных партнёрств.", "цифровых следов граждан.", "нежелательных последствий.",
     "внезапных открытий."]
]

def maketxt():
    txt = table[0][0] + ' '
    fl = False
    for i in range(0, 40):
        for a in range(0, 5):
            if fl:
                rand_a = random.randint(0, 7)
                txt += table[a][rand_a]
                if txt[-1] != '.': txt += ' '
            else:
                if a == 0 and i == 0:
                    fl = True
        if i % 12 == 0:
            txt += '\n'
    print(txt)

def generate_name():
    female_names = ["Анна", "Мария", "Ольга", "Екатерина", "Наталья", "Татьяна", "Александра", "Ирина", "Валерия", "Юлия"]
    male_names = ["Алексей", "Иван", "Максим", "Сергей", "Дмитрий", "Андрей", "Никита", "Артем", "Михаил", "Константин"]
    surnames = ["Иванов", "Смирнов", "Кузнецов", "Попов", "Васильев", "Петров", "Соколов", "Михайлов", "Новиков", "Федоров"]

    # случайный выбор пола
    gender = random.choice(["male", "female"])

    if gender == "male":
        # случайный выбор мужского имени и фамилии
        name = random.choice(male_names)
        surname = random.choice(surnames)
    else:
        # случайный выбор женского имени и фамилии
        name = random.choice(female_names)
        surname = random.choice(surnames) + "а"

    # объединение имени и фамилии
    full_name = name + " " + random.choice(male_names)[0] + ". " + surname

    return full_name

def generate_list():
    array = []
    for i in range(random.randint(3, 15)):
        array.append(generate_name())
    print('\n'.join(str(x) for x in array))

class Room:
    def __init__(self, name, label, description, actions):
        self.name = name
        self.label = label
        self.description = description
        self.actions = actions

class Game:
    def __init__(self, rooms):
        self.rooms = rooms
    def play(self):
        current_room = rooms[0]
        while current_room.label != 'end':
            if (current_room.label == 'start'):
                print('Начало лабиринта!\nВы в начале лабиринта. Сможете ли из него выбраться?')
                print()
            else:
                print(current_room.name)
                print()
                print(current_room.description)
                print()
            print('\n'.join(current_room.actions[i]['name'] for i in range(len(current_room.actions))))
            choice = int(input(">"))
            while choice == 0 or choice > len(current_room.actions):
                print("Проверьте правильность выбора!")
                choice = int(input(">"))
            print("...")
            for room in self.rooms:
                if room.label == (current_room.actions[choice - 1])['dest']:
                    current_room = room
                    break
        print('Выбрались из лабиринта! Красаучик!')


room1 = Room('Начало', 'start', '', [{'name': '1. Проход на Север', 'dest': 'room2'}])
room2 = Room('Комната №2', 'room2', 'Вы находитесь в комнате №2.', [{'name': '1. Проход на Юг', 'dest': 'start'}, {'name': '2. Проход на Запад', 'dest': 'room3'}, {'name': '3. Проход на Север', 'dest': 'room4'}, {'name': '4. Проход на Восток', 'dest': 'room5'}])
room3 = Room('Комната №3', 'room3', 'Вы находитесь в комнате №3.', [{'name': '1. Проход на Восток', 'dest': 'room2'}])
room4 = Room('Комната №4', 'room4', 'Вы находитесь в комнате №4.', [{'name': '1. Проход на Юг', 'dest': 'room2'}, {'name': '2. Проход на Восток', 'dest': 'room6'}])
room5 = Room('Комната №5', 'room5', 'Вы находитесь в комнате №5.', [{'name': '1. Проход на Восток', 'dest': 'room7'}, {'name': '2. Проход на Север', 'dest': 'room6'}, {'name': '3. Проход на Запад', 'dest': 'room2'}])
room6 = Room('Комната №6', 'room6', 'Вы находитесь в комнате №6.', [{'name': '1. Проход на Юг', 'dest': 'room5'}, {'name': '2. Проход на Запад', 'dest': 'room4'}])
room7 = Room('Комната №7', 'room7', 'Вы находитесь в комнате №7.', [{'name': '1. Проход на Юг', 'dest': 'end'}, {'name': '2. Проход на Запад', 'dest': 'room8'}, {'name': '3. Проход на Север', 'dest': 'room9'}])
room8 = Room('Комната №8', 'room8', 'Вы находитесь в комнате №8.', [{'name': '1. Проход на Запад', 'dest': 'room7'}, {'name': '2. Проход на Север', 'dest': 'room10'}])
room9 = Room('Комната №9', 'room9', 'Вы находитесь в комнате №9.', [{'name': '1. Проход на Юг', 'dest': 'room7'}, {'name': '2. Проход на Север', 'dest': 'room12'}, {'name': '3. Проход на Восток', 'dest': 'room10'}])
room10 = Room('Комната №10', 'room10', 'Вы находитесь в комнате №10.', [{'name': '1. Проход на Юг', 'dest': 'room8'}, {'name': '2. Проход на Восток', 'dest': 'room9'}, {'name': '3. Проход на Север', 'dest': 'room11'}])
room11 = Room('Комната №11', 'room11', 'Вы находитесь в комнате №11.', [{'name': '1. Проход на Юг', 'dest': 'room10'}])
room12 = Room('Комната №12', 'room12', 'Вы находитесь в комнате №12.', [{'name': '1. Проход на Юг', 'dest': 'room9'}])
end = Room('Конец', 'end', '', [{'name': 'Проход на Север', 'dest': 'room7'}])

rooms = [room1, room2, room3, room4, room5, room6, room7, room8, room9, room10, room11, room12, end]

def make_graph():
    Graph = graphviz.Digraph(strict=True, graph_attr={'rankdir':'BT'})
    for i in range(1, len(rooms)):
        room = rooms[i - 1]
        for tails in room.actions:
            Graph.edge(room.label, tails['dest'])
    Graph.node('end', fillcolor='green', style='filled')
    Graph.node('start', fillcolor='grey', style='filled')
    Graph.render(filename='graph')

make_graph()


def find_exit_path(rooms, current_room, visited_rooms, path):
    visited_rooms.append(current_room)
    path.append(current_room)
    if current_room.label == 'end':
        return path
    for action in current_room.actions:
        next_room = [room for room in rooms if room.label == action['dest']][0]
        if next_room not in path:
            exit_path = find_exit_path(rooms, next_room, visited_rooms[:], path[:])
            if exit_path:
                return exit_path
    return None

def check_for_dead_ends(game):
    dead_ends = []
    for room in game.rooms:
        exit_path = find_exit_path(game.rooms, room, [], [])
        if not exit_path:
            dead_ends.append(room)
    if dead_ends:
        print('Найдены тупики:')
        for room in dead_ends:
            print(f'Комната "{room.name}" является тупиком.')
    else:
        print('Тупиков нет')

def main():
    print(5.1)
    groups()
    a = input('Продолжить? y/n\t')
    if a == 'n': return
    print(5.2)
    myprint(input('Введите строку для продолжения:'))
    a = input('Продолжить? y/n\t')
    if a == 'n': return
    print(6.1)
    maketxt()
    a = input('Продолжить? y/n\t')
    if a == 'n': return
    print(6.2)
    generate_list()
    a = input('Продолжить? y/n\t')
    if a == 'n': return
    print(7.1)
    Game(rooms).play()
    a = input('Продолжить? y/n\t')
    if a == 'n': return
    print(7.2)
    make_graph()
    print('Граф сохранен!')
    a = input('Продолжить? y/n\t')
    if a == 'n': return
    check_for_dead_ends(Game(rooms))

if __name__ == '__main__':
    main()