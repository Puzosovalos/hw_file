from pprint import pprint

cook_book = {}
with open('recipes.txt') as file:
    for line in file:
        name = line.strip()
        count = int(file.readline())
        ingredients = []
        for elem in range(count):
            d = {}
            ingredient = file.readline().strip()
            d['ingredient_name'], d['quantity'], d['measure'] = (
                ingredient.split(' | ')
            )
            d['quantity'] = int(d['quantity'])
            ingredients.append(d)
        file.readline()
        cook_book[name] = ingredients


def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredients in cook_book[dish]:
                d = {}
                d['measure'] = ingredients['measure']
                d['quantity'] = ingredients['quantity'] * person_count
                result[ingredients['ingredient_name']] = d
        else:
            return 'Такого блюда нет!'
    return result


def write_to_file():
    file1 = open('1.txt')
    file2 = open('2.txt')
    file3 = open('3.txt')
    lines1 = file1.readlines()
    lines2 = file2.readlines()
    lines3 = file3.readlines()
    a = []
    a.append(len(lines1))
    a.append(len(lines2))
    a.append(len(lines3))
    a.sort()
    files = {
        'smallest_file': a[0],
        'middle_file': a[1],
        'biggest_file': a[2],
    }
    output_file = 'result.txt'
    with open(output_file, 'a') as f:
        if len(lines1) == files['smallest_file']:
            f.write(file1.name + '\n')
            f.write(str(len(lines1)) + '\n')
            f.writelines(lines1)
            f.write('\n')
        elif len(lines2) == files['smallest_file']:
            f.write(file2.name + '\n')
            f.write(str(len(lines2)) + '\n')
            f.writelines(lines2)
            f.write('\n')
        elif len(lines3) == files['smallest_file']:
            f.write(file3.name + '\n')
            f.write(str(len(lines3)) + '\n')
            f.writelines(lines3)
            f.write('\n')
        if len(lines1) == files['middle_file']:
            f.write(file1.name + '\n')
            f.write(str(len(lines1)) + '\n')
            f.writelines(lines1)
            f.write('\n')
        elif len(lines2) == files['middle_file']:
            f.write(file2.name + '\n')
            f.write(str(len(lines2)) + '\n')
            f.writelines(lines2)
            f.write('\n')
        elif len(lines3) == files['middle_file']:
            f.write(file3.name + '\n')
            f.write(str(len(lines3)) + '\n')
            f.writelines(lines3)
            f.write('\n')
        if len(lines1) == files['biggest_file']:
            f.write(file1.name + '\n')
            f.write(str(len(lines1)) + '\n')
            f.writelines(lines1)
            f.write('\n')
        elif len(lines2) == files['biggest_file']:
            f.write(file2.name + '\n')
            f.write(str(len(lines2)) + '\n')
            f.writelines(lines2)
            f.write('\n')
        elif len(lines3) == files['biggest_file']:
            f.write(file3.name + '\n')
            f.write(str(len(lines3)) + '\n')
            f.writelines(lines3)
            f.write('\n')
        print(f'Файл сохранен под именем {output_file}')


if __name__ == '__main__':
    pprint(cook_book)
    print('-----------------')
    pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
    print('-----------------')
    write_to_file()
