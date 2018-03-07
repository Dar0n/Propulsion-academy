# Exercise 1
# Race

class Car():

    reduce_fuel_multiplier = 0.2

    def __init__(self, color, tank_size, n_laps, lap_length):
        self.color = color
        self.tank_size = tank_size
        self.n_laps = n_laps
        self.lap_length = lap_length
        self.fuel = tank_size

    def run_laps(self):
        self.n_laps -= 1
        self.fuel -= self.lap_length*self.reduce_fuel_multiplier
        return self.fuel

    def check_pit_stop(self):
        if self.fuel <= 10:
            print("Too little fuel, please re-fill the tank")
        else:
            print("You are good to go")





opel = Car("red", 90, 10, 100)
print(opel.fuel)
print(opel.check_pit_stop())
print(opel.run_laps())
print(opel.n_laps)
print(opel.check_pit_stop())


# Exercise 2
# Books

class Book():

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return "{} by {}".format(self.title, self.author)


class Bookcase():

    def __init__(self, books): # [("Title", "Author")...]
        self.books = self.create_books(books)

    def create_books_lc(self, books):
        return [Book(t,a) for t,a in books]

    def create_books(self, books):
        my_list = []
        for t,a in books:
            my_list.append(Book(t,a))
        return my_list

    def __iter__(self):
        for book in self.books:
            yield str(book)



book1 = ("Title1", "Author1")
book2 = ("Title2", "Author2")
book3 = ("Title3", "Author3")

book_list = [book1, book2, book3]

bookcase1 = Bookcase(book_list)
for book in bookcase1:
    print(book)


# Exercise 3
# Water molecule


print("")
print("")
print("Exercise 3 - water molecule")
print("")
print("")

# Creating class for quarks

class Quark():

    charges = {
        "Up": 0.666,
        "Down": -0.333
    }

    def __init__(self,type):
        self.type = type
        self.charge = self.charges[self.type]
        self.symbol = type[0:1]

    def __str__(self):
        return "Type: {}; Charge: {}\nSymbol: {}".format(self.type, self.charge, self.symbol)

# up_quark = Quark("Up")
# print(str(up_quark))
# down_quark = Quark("Down")
# print(str(down_quark))
# print("\n#######################\n")

# Creating class for nucleons

class Nucleon():
    con = {
        "Proton": ["Up", "Up", "Down"],
        "Neutron": ["Up", "Down", "Down"]
    }



    def __init__(self, type):
        self.type = type
        self.quarks_list = []
        self.quarks = self.add_quarks()
        self.charge = self.calculate_charge()
        self.symbol = type[0:1]

    def show_symbol(self):
        return self.symbol

    def calculate_charge(self):
        temp_charge = 0
        for quark in self.quarks_list:
            temp_charge += quark.charge
        return round(temp_charge)


    def add_quarks(self):
        for type in self.con[self.type]:
            self.quarks_list.append(Quark(type))
        return self.quarks_list

    def __str__(self):
        return "The {} contains {} quarks - {} with +1e elementary charge".format(self.type, len(self.quarks_list), self.type)

# proton = Nucleon("Proton")
# print(str(proton))
# print(proton.charge)
# neutron = Nucleon("Neutron")
# print(str(neutron))
# print(neutron.charge)





print("\n#######################\n")
# Creating class for atoms

class Atom():

    proton_mass = 1.007
    neutron_mass = 1.008

    con = {
        "Oxygen": {"Proton": 8, "Neutron": 8},
        "Hydrogen": {"Proton": 1, "Neutron": 0}
    }

    consts = {
        "Oxygen": ["1 1 1", -2],
        "Hydrogen": ["2 2 2", 1]
    }

    def __init__(self, name):
        self.name = name
        self.nucleons_list = []
        self.atomic_number = self.get_atomic_number()
        self.atomic_mass = self.get_atomic_mass()
        self.position = self.get_position()
        self.charge = self.get_charge()
        self.symbol = self.name[0:1]
        self.nucleons = self.add_nucleons()

    def get_atomic_number(self):
        return self.con[self.name]["Proton"]*self.proton_mass

    def get_atomic_mass(self):
        return self.con[self.name]["Proton"]*self.proton_mass + self.con[self.name]["Neutron"]*self.neutron_mass

    def atom_symbol(self):
        return self.symbol

    def get_charge(self):
        return self.consts[self.name][1]

    def get_position(self):
        return self.consts[self.name][0]

    def add_nucleons(self):
        for key, val in self.con[self.name].items():
            for i in range(val):
                self.nucleons_list.append(Nucleon(key))
        return self.nucleons_list


    def __str__(self):
        return "Name: {}\nDescription:\n - Atomic number: {}\n - Atomic mass: {}\n - Position: {}\n - Charge: {}".format\
            (self.name, self.atomic_number, self.atomic_mass, self.position, self.charge)

# oxygen_atom = Atom("Oxygen")
# print(oxygen_atom.position)
# hydrogen_atom = Atom("Hydrogen", 0.999, 0.999, "2 2 2", 1)
# print(str(hydrogen_atom))


print("\n#######################\n")
# Creating class for molecule of water

class Molecule():

    con = {
        "Hydrogen": 2,
        "Oxygen": 1
    }

    def __init__(self):
        self.name = "Water"
        self.list_atoms = []
        self.atoms = self.add_atoms()


    def add_atoms(self):
         for key, val in self.con.items():
             for i in range(val):
                self.list_atoms.append(Atom(key))
         return self.list_atoms

    def show_atoms(self):
        return self.atoms

    def __str__(self):
        result = "\nThis is a molecule named {} and it has {} atoms.\nThe atoms are:\n".format(self.name, len(self.atoms))
        for i in range(len(self.atoms)):
            result = result + "\n" + str(i+1) + " " + str(self.atoms[i])
        # print("result is" + result)
        return result

# water = Molecule()
# print(water.atoms[2])
# print(str(water))
# print(water.atoms[2].nucleons[4].quarks)



######################################

# Exercise 4
# Inheritance

# Class for basic shape

class Shape:
    def __init__(self, x, y, real):
      self.center = (x,y)
      self.real = real

    def get_area(self):
      # empty shape does not have an area -> return 0
      return 0

    def is_real(self):
        if self.real:
            return 1
        else:
            return -1

print("\n####################\n")
# Class for circle

class Circle(Shape):

    PI = 3.1415

    def __init__(self,x , y, real, r):
        super().__init__(x, y, real)
        self.radius = r
        #self.shape_area = 0
        self.area = self.get_area()


    def get_area(self):
        # self.shape_area =  self.PI*self.radius*self.radius
        # return self.shape_area
        return self.is_real()*self.PI*self.radius*self.radius

class Rectangle(Shape):
    def __init__(self,x, y, real, width,height):
        super().__init__(x, y, real)
        self.width = width
        self.height = height
        self.area = self.get_area()

    def get_area(self):
        return self.is_real()*self.width*self.height

class Triangle(Shape):
    def __init__(self, x, y, real, base, height):
        super().__init__(x, y, real)
        self.base = base
        self.height = height
        self.area = self.get_area()

    def get_area(self):
        return self.is_real()*0.5*self.base*self.height




class House():

    def __init__(self, n_walls, n_roof_tops):
        self.n_walls = n_walls
        self.n_roof_tops = n_roof_tops
        self.walls = self.get_walls()
        self.roof_tops = self.get_roof_tops()
        self.holes = self.get_holes()
        self.area = self.get_area()

    def get_walls(self):
        return [Rectangle(2,1.5,True,4,3) for i in range(self.n_walls)]

    def get_roof_tops(self):
        return [Triangle(2,4,True,4,2) for i in range(self.n_roof_tops)]

    def get_holes(self):
        holes = []
        for wall in self.walls:
            holes.append(Rectangle(1, 1, False, 1, 2))
            holes.append(Rectangle(3, 2, False, 1,1))
        for roof_top in self.roof_tops:
            holes.append(Circle(2, 4, False, 0.75))
        return holes

    def get_area(self):
        total_area = 0
        for wall in self.walls:
            total_area += wall.area
            print(total_area)
        for roof_top in self.roof_tops:
            total_area += roof_top.area
            print(total_area)
        for hole in self.holes:
            total_area += hole.area
            print(total_area)
        return total_area


house = House(2,2)

print(house.area)

