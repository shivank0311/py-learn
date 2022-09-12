class animal:
    def talk(self): print("i have to say")
    def walk(self): print ("i am walking")
    def clothes(self): print("i have clothes")

class Duck(animal):
    def quack(self):
        print("quaccck")

    def walk(self):
        super().walk()

class dog(animal):
    def clothes(self):
        print("i have black fur")

def main():
    donald = Duck()
    donald.quack()
    donald.walk()
    donald.clothes()

    fido = dog()
    fido.walk()
    fido.clothes()

if __name__=="__main__" : main()   