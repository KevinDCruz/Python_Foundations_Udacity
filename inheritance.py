class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor Called")
        self.lastname = last_name
        self.eyecolor = eye_color

    def show_info(self):
        print("Last Name:"+self.lastname)
        print("Eye color:"+self.eyecolor)


class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child constructor called")
        Parent.__init__(self, last_name, eye_color)
        self.toys = number_of_toys

    def show_info(self):
        print("Last Name:"+self.lastname)
        print("Eye color:"+self.eyecolor)
        print("Number of Toys:"+str(self.toys))

billy_cyrus = Parent("Cyrus","Green")
print(billy_cyrus.lastname)

miley_cyrus = Child("Cyrus", "green", 2)
print(miley_cyrus.lastname)
print(miley_cyrus.toys)
print(miley_cyrus.show_info())