
#*****************************************FIRST_HW******************************************************************************************************

class Student:
    def __init__(self, name, surname, city, age, email):
        self.name = name
        self.surname = surname
        self.city = city
        self.age = age
        self.email = email

    def __str__(self):
        return f'name : {self.name}\n' \
               f'surname: {self.surname}\n' \
               f'city: {self.city}' \
               f'age : {self.age}\n' \
               f'email: {self.email}$\n' \
               f'Age: {self.age}'

    def study(self):
        return f"My name is {self.name}"


student1 = Student(name="Ivan", surname="Alekseev", city="Moscow", age=22, email="alex@gmail.com")
student2 = Student(name="Nursultan", surname="Samatov", city="Bishkek", age=19, email="n.samatov@gmail.com")
student3 = Student(name="Sam", surname="Kobi", city="New York", age=24, email="samkobi@gmail.com")

print(student1)
print(student2)
print(student3)


class Trainee(Student):
    def __init__(self,  name, surname, city, age, email, project_name, language):
        super(Trainee, self).__init__(name, surname, city, age, email)
        self.project_name = project_name
        self.language = language

    def __str__(self):
        return f'project_name : {self.project_name}\n' \
               f'language: {self.language}\n' 

    def code(self):
        return f"I code in {self.language} programming language!"


tr1 = Trainee(name="Ivan", surname="Alekseev", city="Moscow", age=22, email="alex@gmail.com",
                    project_name="New Era", language="C++")

tr2 = Trainee(name="Nursultan", surname="Samatov", city="Bishkek", age=19, email="n.samatov@gmail.com",
                    project_name="Shop", language="Python")

print(tr1)
print(tr2)


class TeamLead(Trainee):
    def __init__(self,  name, surname, city, age, email, project_name, language, company_name, team):
        super(TeamLead, self).__init__( name, surname, city, age, email, project_name, language)
        self.company_name = company_name
        self.team = team

    def __str__(self):
        return f'company_name : {self.company_name}\n' \
               f'team: {self.team}\n'

    def leader(self):
        return f"I have {len(self.team)} people in my team"


tl1 = TeamLead(name="Ivan", surname="Alekseev", city="Moscow", age=22, email="alex@gmail.com", project_name="New Era", language="C++",
                company_name="Sky Building", team=["Kostya", "Alex", "Lena", "Kiril"])
tl2 = TeamLead(name="Nursultan", surname="Samatov", city="Bishkek", age=19, email="n.samatov@gmail.com", project_name="Shop", language="Python",
                company_name="IT house", team=["Esen", "Pasha", "Kamila"])

print(tl1)  
print(tl2)


# #*****************************************SECOND_HW******************************************************************************************************
class Auth:

    def _check_username(self):
        print('Checking username...')

    def __check_password(self):
        print('Checking password...')

study = Auth()
study._check_username()
# study.__check_password()

#*****************************************THIRD_HW******************************************************************************************************

class Russian:

    def say_hello(self):
        return f'Привет'


class English:

    def say_hello(self):
        return f'Hello'


class Turkish:

    def say_hello(self):
        return f'Merhaba'


ru = Russian()
en = English()
tu = Turkish()

print(ru.say_hello(), en.say_hello(), tu.say_hello())


#*****************************************FOURTH_HW******************************************************************************************************


class Version1:
    def updates(self):
        print('Fixed bags')


class Version2(Version1):
    def updates(self):
        print('Added profile')


class Version3(Version2):
    def updates(self):
        print('Optimized')


v1 = Version1()
v1.updates()

v2 = Version2()
v2.updates()

v3 = Version3()
v3.updates()




