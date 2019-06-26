from abc import ABC, abstractmethod
class Animal(ABC):
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

    @abstractmethod
    def collect(self):
        """
        Собрать породукт
        :return: None
        """
        print(self.name, end=': ')



class Bird(Animal):
    """
    Класс птица, для описания общий функций для этого вида животных
    """
    def __init__(self, name, weight, voice):
        super().__init__(name, weight, voice)

    def collect(self):
        """
        Собрать яйца
        :return: None
        """
      super().collect()
      print('Мои яйци собраны')


class Milking(Animal):
    """
    Класс для животных, которых можно доить
    """
    def __init__(self, name, weight, voice):
        super().__init__(name, weight, voice)

    def collect(self):
        """
        Подоить
        :return: None
        """
      super().collect()
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
    Можно подстричь
    """
    def __init__(self, name, weight):
        super().__init__(name, weight, 'Bheee-eee')

    def collect(self):
        """
        Подстричь
        :return: None
        """
      super().collect()
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
goose_white = Goose('Белый', 9)
cow_manya = Cow('Маня', 50)
goat_roga = Goat('Рога', 25)
goat_kop = Goat('Копыта', 23)
chicken_koko = Chicken('Ко-ко', 5)
chicken_kuka = Chicken('Кукареку', 5)
sheep_barash = Sheep('Барашек', 25)
sheep_kudr = Sheep('Кудрявый', 23)
duck_krya = Duck('Кряква', 6)

all_animals = {goose_grey, goose_white, cow_manya, goat_roga, goat_kop,
               chicken_koko, chicken_kuka, sheep_barash, sheep_kudr, duck_krya}


total_weight = 0
max_weight = float('-inf')

for animal in all_animals:
    animal.do_eat()
    animal.collect()
    total_weight += animal.weight
    if max_weight > animal.weight:
        max_weight = animal.weight

print('Общий вес животных:', total_weight)
print('Самый большой вес:', max([x.weight for x in all_animals]))
