class Client:

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

    def get_name(self):
        return self.name

    def get_clients(self):
        return self.name,self.age,self.id