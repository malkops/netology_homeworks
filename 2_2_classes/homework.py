class Animal:
    """
    Главный класс животное
    Имеет два метода: подать голос и покушать
    Имеет две переменные: имя и вес
    """
    def __init__(self, name, weight, voice):
        self.name = name
        self.weight = weight
        self.voice = voice

    def make_voice(self):
        """
        Подать голос
        :return: None
        """
        print(self.name, end=': ')
        print(self.voice)

    def do_eat(self):
        """
        Покушать
        :return: None
        """
        print(self.name, end=': ')
        print('Меня накормили')


class Bird(Animal):
    """
    Класс птица, для описания общий функций для этого вида животных
    """
    def __init__(self, name, weight, voice):
        super().__init__(name, weight, voice)

    def collect_egs(self):
        """
        Собрать яйца
        :return: None
        """
        print(self.name, end=': ')
        print('Мои яйци собраны')


class Milking(Animal):
    """
    Класс для животных, которых можно доить
    """
    def __init__(self, name, weight, voice):
        super().__init__(name, weight, voice)

    def do_milking(self):
        """
        Доить
        :return: None
        """
        print(self.name, end=': ')
        print('Меня подоили')


class Cow(Milking):
    """
    Класс корова, наследуется от Animal и Milking
    Можно подоить
    """
    def __init__(self, name, weight):
        super().__init__(name, weight, 'Mo-mo mo-motherf*cker')


class Goat(Milking):
    """
    Класс коза, наследуется от Milking
    Можно подоить
    """
    def __init__(self, name, weight):
        super().__init__(name, weight, 'Mheee-eee')


class Sheep(Animal):
    """
    Класс овца, наследуется от Animal
    Можно подстрич
    """
    def __init__(self, name, weight):
        super().__init__(name, weight, 'Bheee-eee')

    def shear(self):
        """
        Подстрич овцу
        :return: None
        """
        print(self.name, end=': ')
        print('Меня подстригли. Теперь я лысый!!!')


class Goose(Bird):
    """
    Класс гусь, наследуется от Bird
    """
    def __init__(self, name, weight):
        super().__init__(name, weight, 'The unique sound of goose')


class Chicken(Bird):
    """
    Класс курица, наследуется от Bird
    """
    def __init__(self, name, weight):
        super().__init__(name, weight, 'Ko-ko-ko. Кто на турник?')


class Duck(Bird):
    """
    Класс утка, наследуется от Bird
    """
    def __init__(self, name, weight):
        super().__init__(name, weight, 'Кря!')


goose_grey = Goose('Серый', 10)
goose_grey.do_eat()
goose_grey.collect_egs()
goose_white = Goose('Белый', 9)
goose_white.do_eat()
goose_white.collect_egs()
cow_manya = Cow('Маня', 50)
cow_manya.do_eat()
cow_manya.do_milking()
goat_roga = Goat('Рога', 25)
goat_roga.do_eat()
goat_roga.do_milking()
goat_kop = Goat('Копыта', 23)
goat_kop.do_eat()
goat_kop.do_milking()
chicken_koko = Chicken('Ко-ко', 5)
chicken_koko.do_eat()
chicken_koko.collect_egs()
chicken_kuka = Chicken('Кукареку', 5)
chicken_kuka.do_eat()
chicken_kuka.collect_egs()
sheep_barash = Sheep('Барашек', 25)
sheep_barash.do_eat()
sheep_barash.shear()
sheep_kudr = Sheep('Кудрявый', 23)
sheep_kudr.do_eat()
sheep_kudr.shear()
duck_krya = Duck('Кряква', 6)
duck_krya.do_eat()
duck_krya.collect_egs()

all_animals = {goose_grey, goose_white, cow_manya, goat_roga, goat_kop,
               chicken_koko, chicken_kuka, sheep_barash, sheep_kudr, duck_krya}

total_weight = 0
max_weight = float('-inf')

for animal in all_animals:
    total_weight += animal.weight
    if max_weight > animal.weight:
        max_weight = animal.weight

print('Общий вес животных:', total_weight)
print('Самый большой вес:', max([x.weight for x in all_animals]))
