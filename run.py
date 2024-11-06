class Tomato:
    states = {0: 'Отсутствует', 1: 'Цветение', 2: 'Зеленый', 3: 'Красный'}
    def __init__(self, index):
        self._index = index # защищенный атрибут
        self._state = 0 # защищенный атрибут
        # Два динамических свойства
        
    
    def grow(self): # Переход на следущую стадию созревания
        self._state += 1
            
    
    def is_ripe(self): # Провекра зрелости
        return self._state == 3
        
        
class TomatoBush:
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(0, num)]
        
    def grow_all(self):
        for i in self.tomatoes:
            i.grow()
            
    def all_are_ripe(self):
        return all([i.is_ripe() for i in self.tomatoes])
        
    
    def give_away_all(self):
        self.tomatoes = []
        


class Gardener:
    def __init__(self, name, plant):
        self.name = name # публичный атрибут
        self._plant = plant # защищенный атрибут
        
    def work(self):
        self._plant.grow_all()
        
    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Урожай собран")
        else:
            print("Урожай не готов")
        
    @staticmethod
    def knowledge_base(name):
        return f"Имя садовника: {name}\nСадовник знает следующие команды: work, harvest"
        
        
print(Gardener.knowledge_base(("Иван")))
bush = TomatoBush(4)
gardener = Gardener("Иван", bush)
gardener.work()
gardener.harvest()
gardener.work()
gardener.work()


gardener.harvest()

        
    