from pprint import pprint


class Product:

    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category
        # print(vars(self))

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        # print('get_products ')
        file = open(self.__file_name, 'r')
        stroka = file.read()
        # print('читаем файл ', stroka)
        file.close()
        return stroka

    def _add(self, *products):
        # print('добавляем товар', *products, 'товара ',len(products), 'штуки')
        stroka = self.get_products()
        if len(stroka) == 0:
            print('Открываем магазин!')
        prihod = [*products]
        for i in range(len(products)):
            file = open(self.__file_name, 'a')
            tovar = str(prihod[i])
            if tovar in stroka:
                # name = tovar[0: tovar.find(',')]
                # print(f'Продукт {name} уже есть в магазине')
                print(f'Продукт {tovar} уже есть в магазине')
                continue
            # print('Записываем ', tovar)
            file.write(tovar + '\n')
            file.close()


def test():
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')
    print(s1.get_products())
    # print(str(p2))
    s1._add(p1, p2, p3)
    print(s1.get_products())
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')
    s1._add(p1, p2, p3)
    print(s1.get_products())


if __name__ == '__main__':
    test()
