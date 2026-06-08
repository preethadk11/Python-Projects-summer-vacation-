class student:
    def __init__(self,name,age,department):
       self.name=name
       self.age=age
       self.department=department
    def introduce(self):
        print(f"Hi, I'm {self.name}")
        print(f"I'm {self.age} years old")
        print(f"I study {self.department}")
s1=student("Preetha",19,"cs")
s2=student("Anu",20,"ai")
s1.introduce()
print()
s2.introduce()