import os

cook_book = dict()

with open('recipes.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    list = []
    result = []
    n = '\n'
    for l in lines:
        if l == '\n':
            list += l
            result.append(list)
            list = []
        else:
            list.append(l)
    result.append(list)

for cook_list in result:
    ingredient_list = []

    for list_ in cook_list:
        list = list_.replace('\n', '')
        if "|" in list:
            ing_list = list.split(' | ')
            ingredient_list.append(ing_list)
    ing_list = []

    for ing_list_2 in ingredient_list:
        ing_dict = dict()
        if ing_list_2:
            ing_dict['ingredient_name'] = ing_list_2[0]
            ing_dict['quantity'] = ing_list_2[1]
            ing_dict['measure'] = ing_list_2[2]
        ing_list.append(ing_dict)
        cook_book[cook_list[0].replace('\n', '')] = ing_list


def get_shop_list_by_dishes(dishes: list, person_count: int) -> dict:
    """Функция обрабатывает список блюд и количество персон.

    :param dishes: Список блюд.
    :param person_count: Количество человек.
    :return: Выводит на экран список ингредиентов
    для приготовления всех блюд.
    """
    food_basket = {}
    for dish in dishes:
        if dish not in cook_book:
            raise TypeError(f'{dish} отсутствует в кулинарной книге')
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] not in food_basket:
                food_basket[ingredient['ingredient_name']] \
                    = {'measure': ingredient['measure'], 'quantity': \
                    int(ingredient['quantity']) * person_count}
            else:
                food_basket[ingredient['ingredient_name']]['quantity'] \
                    += int(ingredient['quantity']) * person_count
    return food_basket


def get_dirs_and_files():
    """ Функция создает ссылку "dirs" на заданную директорию и
    создает список файлов в ней.

    :return: Вызывает функцию get_len_files() и передает
    подготовленные данные."""
    path = os.path.join(os.getcwd() + '\sorted/')
    result = os.walk(path)
    for dirs, folder, files in result:
        dirs_ = dirs
        files_ = files
    return get_len_files(dirs_, files_)


dict_lens_and_files = dict()


def get_len_files(dirs, files):
    """ Функция создает словарь. Ключами словаря являются количкество
    строк в файлах, а значениями имена файлов соответственно.

    :param dirs: Ссылка на заданную директорию.
    :param files: Список файлов в заданной папке.
    :return: Вызывает функцию sorted_files_dict()."""
    for file in files:
        file_path = dirs + file
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            file_len = len(lines)
            dict_lens_and_files[file_len] = file
    return sorted_files_dict()


sorted_dict = dict()


def sorted_files_dict():
    """ Функция сортирует словарь по ключу.
    :return: Вызывает функцию save_sorted_files()."""
    sorted_dict.update(dict(sorted(dict_lens_and_files.items())))
    return save_sorted_files()


def save_sorted_files():
    """ Функция записывает информацию о всех файлах и текст из самих файлов
    из заданной папки в новый файл.
    Каждый раз файл удаляется и создается заново.
    :return: Результат всей операции выводится на экран."""
    file_link = os.path.join(os.getcwd(), 'file.txt')
    os.remove(file_link)
    for file_num in sorted_dict:
        file_for_link = sorted_dict.get(file_num)
        file_link_ = os.path.join(os.getcwd() + '\sorted/', file_for_link)
        h1 = sorted_dict.get(file_num)
        with open(file_link_, 'rt', encoding='utf-8') as fl:
            lines = fl.readlines()
            with open(file_link, 'a+') as f:
                f.write(f'{h1}\n')
                f.write(f'{file_num}\n')
                for line in lines:
                    f.write(line.strip())
                    f.write(f'\n')
                    f.flush()
    with open('file.txt') as f1:
        result = f1.read()
    return result


print()
print()

# Вызываем функцию по получению списка продуктов из кулинарной
# книги согласно списку блюд
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 2))

print()
print()

# Вызываем функцию для последующей сортировки и объединения
# текстовых файлов в один
print(get_dirs_and_files())
