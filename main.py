from csv import reader


def parse_file(file):
    with open(file) as monsters:
        csv_reader = reader(monsters)
        return list(csv_reader)


def parse_monsters(monsters):
    clean_monsters = []
    for index, value in enumerate(monsters):
        # print(value[1])
        if value[1] not in clean_monsters:
            clean_monsters.append(value[1])
    return clean_monsters


if __name__ == '__main__':
    monsters = parse_file('Data/D&D Monsters.csv')
    clean_monsters = parse_monsters(monsters)
    print(clean_monsters)
