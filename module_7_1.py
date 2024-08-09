import weight


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name, self.weight, self.category}'


class Shop:
    def __init__(self):
        self.products = None
        self.__file_name = 'products.txt'

    def get_file_name(self):
        return self.__file_name

    def get_products(self):
        name = self.__file_name
        file = open(name, 'r')
        s = file.read()
        file.close()
        return s

    def add(self, *products):

        for i in range(0, len(products)):
            if products[i].name not in self.get_products():
                file = open(self.get_file_name(), 'a')
                file.write(f'\n{products[i].name, products[i].weight, products[i].category}'
                           .replace(')', '').replace('(', '')
                           .replace('', ''))
                file.close()
            else:
                print(f'Продукт {products[i].name} уже есть в магазине')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
