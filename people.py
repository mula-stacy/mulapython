class people:
    def __init__(self, name, age, gender):
        self.peoplename = name
        self.peopleage = age
        self.peoplegender = gender

    def display(self):
        print(self.peoplename, self.peopleage, self.peoplegender)


mymethod = people("Alex", 21, "male")
mymethod1 = people("Salma", 19, "female")
mymethod2 = people("Bilha", 30, "female")
mymethod3 = people("ichalai", 33, "male")
mymethod4=people("nancy",19,"female")
mymethod.display()
mymethod1.display()
mymethod2.display()
mymethod3.display()
mymethod4.display()
