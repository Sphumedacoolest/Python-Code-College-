class Myself:
    """Information about myself"""

    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby

    def introduce(self):
        return f"My name is {self.name}, I am {self.age} years old, and I enjoy {self.hobby}."

class MyChild(Myself):
    """Information about my child, inherited from me"""

    def __init__(self, child_name, child_age, child_hobby):
        super().__init__(child_name, child_age, child_hobby)
        self.name = child_name
        self.age = child_age
        self.hobby = child_hobby

    def introduce(self):
        return f"My name is {self.name}, I am {self.age} years old, I enjoy {self.hobby}."

Cj = MyChild("CJ","8", "playing games")
print(Cj.introduce())

Sphume = Myself('Sphume', '19', 'reading')
print(Sphume.introduce())