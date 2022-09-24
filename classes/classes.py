class Duck:
    def __init__(self,**kwargs):
        self.variables = kwargs

    def quack(self):
        print ("Quacck")

    def walk(self):
        print ("walk like a duck")

    def set_variables(self,k,v):
        self.variables[k]= v 

    def get_variables(self,k):
        return self.variables.get(k, none)

def main():
    donald= Duck(feet= 2)
    donald.set_variable("color","blue")
    print(donald.get_variable ("feet"))
    print(donald.get_variable("color"))

if __name__=="__main__": main()
