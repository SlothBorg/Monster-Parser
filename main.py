def parse_file(file):
    with open(file) as monsters:
        return monsters.read().splitlines()


def print_monsters(monsters):
    for index, value in enumerate(monsters):
        if index % 4 == 0:
            print(parse_values(index, monsters))


def parse_values(index, array):
    return array[index] + '\t' + array[index+1] + '\t' + array[index+2] + '\t' + array[index+3]


if __name__ == '__main__':
    monsters = parse_file('monsters.txt')
    print_monsters(monsters)
