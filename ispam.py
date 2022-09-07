class Spam:
    numInstances = 0 # Использлвание статического  метода для данных класса
    def __init__(self):
        Spam.numInstances += 1
    def printNum():
        print(f"Num is: {Spam.numInstances}") # Количество экземпляров
    printNum = staticmethod(printNum)

a = Spam()
b = Spam()
c = Spam()
Spam.printNum() # Вызывается как простая функция 
a.printNum() # Аргумент экземпляра не передается

class Sub(Spam):
    def printNum(): # Переопределение статического метода
        print("Extra stuff...") # С вызовом первоначального класса
        Spam.printNum()
    printNum = staticmethod(printNum)

n = Sub()
m = Sub()
n.printNum() # Вызов из экземпляра подкласса
Sub.printNum() # Вызов из самого класса
Spam.printNum() # Вызов первоначальной версии

class Other(Spam):
    pass

l = Other()
l.printNum() # Наследование статического метода
