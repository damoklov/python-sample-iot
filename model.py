from abc import ABC, abstractmethod

class AbstractParent(ABC):
  @abstractmethod
  def hello_friend():
    raise NotImplementedError

class Friend:
    pass

class Mother(AbstractParent):
  def init(self, age=0):
    self.age = age
    print('Mother constructor!')

  @staticmethod
  def order_song():
      Father.play_guitar()

  def do_work(self):
    print("I'm working")

class Father(AbstractParent):
  def init(self):
    print('Father constructor!')

  @staticmethod
  def play_guitar():
    print('play guitar')


class Daughter(Mother, Father):
  def init(self, age = 0):
    Mother.init(self, age=age)
    Father.init(self)

  def do_work(self):
    print("I'm working like a horse!")

  def hello_friend(self):
    pass


def greet_mother(mother : Mother):
  print("Hello mother!!!")
  mother.do_work()


def greet_father(father : Father):
  print('Hello father!!!')
  father.play_guitar()



if __name__ == '__main__':
    daughter = Daughter()
    greet_father(daughter)  # Polymorphism
    greet_mother(daughter)  # Polymorphism
    Mother.order_song()
