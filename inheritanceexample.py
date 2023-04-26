class animal:
    def __init__(self,name):
      self.myname=name

    def talk(self):
        raise NotImplementedError("subclass must implement abstract method")

class Cat(animal):
    def talk(self):
        return "Meow"
class cow(animal):
    def talk(self):
        return "Moo"
class jogoo(animal):
    def talk(self):
        return "crows"
class horse(animal):
    def talk(self):
        return "whine"
class pig(animal):
    def talk(self):
        return "oink"

paka=Cat("Whiskers")
cow=cow("jedi")
jogoo=jogoo("hellen")
horse=horse("alolo")
pig=pig("fati")

print(paka.myname+" :"+paka.talk())
print(cow.myname+" :"+cow.talk())
print(jogoo.myname+" :"+jogoo.talk())
print(horse.myname+" :"+horse.talk())
print(pig.myname+" :"+pig.talk())