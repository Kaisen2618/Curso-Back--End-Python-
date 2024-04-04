#Definindo uma classe base (superclasse)

class Animal:
    def falar(self):
        pass

# Criando classes derivadas (subclasse)
    
class Cachorro(Animal):
    def falar(self):
            return "Woof!\n"
        
class Gato(Animal):
    def falar(self):
            return "Miau!\n"
        
class Cavalo(Animal):
    def falar(self):
         return "HIHIHIHI!\n"
        
#Utilizando Polimorfismo

animais = [Cachorro(), Gato(), Cavalo()]

for animal in animais:
    print(f"{animal.__class__.__name__}: {animal.falar()}")