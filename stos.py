class Stos:
    def __init__(self):
        self.__data = []

    def push(self, elem):
        self.__data.append(elem)

    def pop(self):
        try:
            elem = self.__data[-1]
            del self.__data[-1]
            return elem
        except:
            return 'stos jest pusty!'

    def len(self):
        return len(self.__data)

stos = Stos()
stos.push(4)
stos.push("test")
print(stos.pop()) #test
stos.push(5)
while stos.len():
    print(stos.pop()) # 5, 4
print(stos.pop())
