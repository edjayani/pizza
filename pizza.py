import click
import decorator
import functools
import random


def log(text=str, text2=str):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            p = random.randint(1, 42)
            result = func(*args, **kwargs)
            print(f" {text}{p}{text2}")
        return wrapper
    return decorator


@click.group()
def cli():
    pass


class pizzas:

    def __init__(self, name: str, size: str):
        self.name = name,
        self.size = size,
        self.ingredients = []

    def classify(name):
        """Определяет состав по названию"""
        if name == 'Margherita':
            ingredients = ['tomato sause', 'mozzarella', 'tomatoes']
        elif name == 'Pepperoni':
            ingredients = ['tomato sause', 'mozzarella', 'pepperoni']
        else:
            ingredients = ['tomato sause', 'mozzarella', 'chicken', 'pineapples']
        return ingredients

    def width(size):
        """Определяет ширину пиццы"""
        if size == 'L':
            width1 = 35
        elif size == 'XL':
            width1 = 40
        return width1

    def menu_show():
        """Shows menu"""
        variants = {'Margherita🧀': pizzas.classify('Margherita🧀'), 'Pepperoni🍕': pizzas.classify('Pepperoni🍕'),
                    'Hawaiian🍍': pizzas.classify('Hawaiian🍍')}
        return variants


@log('🍳Приготовили за ', 'с!')
def bake(name: str):
    """ Cooks your pizza"""


@log('🛴Доставили за ', 'с!')
def deliver(name):
    """Delivers your pizza"""


@log('🏠Подождали Вас всего ', 'с!')
def pickup(name):
        """Pickups your pizza"""


#@cli.command()
#@click.option(' =delivery', default=False, is_flag=True)
def order(meal: str):       #Не поняла принцип работы, поэтому убрала delivery: bool из аргументов
    """Обрабатывает Ваш заказ"""
    bake(meal)
    #if delivery == True:
    deliver(meal)
    pickup(meal)

#@cli.command()
def menu():
    """Показывает блюда и их состав"""
    positions = pizzas.menu_show()
    print(positions)
    for key in positions:
        print(key, ':', end = ' ')
        for ingr in positions[key]:
            print(ingr, ',', end = ' ')
        print()


if __name__ == "__main__":
    #cli()
    order('Margherita')



