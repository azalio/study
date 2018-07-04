from abc import ABC


class Hero:
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []

        self.stats = {
            "HP": 128,
            "MP": 42,
            "SP": 100,

            "Strength": 15,
            "Perception": 4,
            "Endurance": 8,
            "Charisma": 2,
            "Intelligence": 3,
            "Agility": 8,
            "Luck": 1
        }

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()


class AbstractEffect(Hero, ABC):
    def __init__(self, base):
        self.base = base

    def get_stats(self):  # Возвращает итоговые хараетеристики
        # после применения эффекта
        pass

    def get_positive_effects(self):
        pass

    def get_negative_effects(self):
        pass


class AbstractPositive(AbstractEffect):
    def get_positive_effects(self):
        pass


class Blessing(AbstractPositive):
    """
    Благословение — Увеличивает все основные характеристики на 2.
    """
    pass


class Berserk(AbstractPositive):
    """
    Берсерк — Увеличивает параметры Сила, Выносливость, Ловкость, Удача на 7; уменьшает параметры Восприятие, Харизма,
    Интеллект на 3. Количество единиц здоровья увеличивается на 50.
    """


class AbstractNegative(AbstractEffect):
    def get_negative_effects(self):
        pass


class Weakness(AbstractNegative):
    """
    Слабость — Уменьшает параметры Сила, Выносливость, Ловкость на 4.
    """
    pass


class Curse(AbstractNegative):
    """
    Сглаз — Уменьшает параметр Удача на 10.
    """
    pass


class EvilEye(AbstractNegative):
    """
    Проклятье — Уменьшает все основные характеристики на 2.
    """
    pass


if __name__ == '__main__':
    hero = Hero()
    print(hero.get_stats())
    print(hero.get_positive_effects())
    print(hero.get_negative_effects())

    bless = Blessing(hero)
    print(bless.get_positive_effects())
    print(bless.get_stats())
