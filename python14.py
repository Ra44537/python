# class Student:
#     def __init__(self, name):
#         self.name = name


# s1 = Student("shraddha")
# print(s1.name)
# del s1.name
# print(s1.name)        


# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.__acc_no = acc_no
#         self.acc_pass = acc_pass

# s1 = Account("12453", "12bcde")       
# print(s1.__acc_no) 



# class person:
#     __name = "anonymous"

#     def __hello(self):
#         print("hello person")

#     def welcome(self):
#         self.__hello()


# p1 = person()

# print(p1.welcome())



# class Car:
#     @staticmethod
#     def start():
#         print("car started..")

#     def stop():
#         print("car stop")

# class Toyota(Car):
#     def __init__(self, name):
#         self.name = name


# c1 = Toyota("fortuner")
# c2 = Toyota("prius")

# print(c1.name)
# print(c1.start())
# print(c2.start)


#multiple inheritance
# class Car:
#     @staticmethod
#     def start():
#         print("car started..")

#     def stop():
#         print("car stop")

# class Toyota(Car):
#     def __init__(self, brand):
#         self.brand = brand

# class Fortuner(Toyota):
#     def __init__(self, type):
#         self.type = type


# c1 = Fortuner("diesel")
# print(c1.type)   
# c1.start()    




# #multi-level inheritance
# class A:
#     varA = "welcome to class A"

# class B:
#     varB = "welcome to class B"

# class C(A,B):
#     varC = "welcome to class c"


# c1 = C()

# print(c1.varC)
# print(c1.varB)







# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def showNumber(self):
#         print(self.real,"i + ", self.img,"j ")   

#     def __add__(self, num2):
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return Complex(newReal, newImg)     

# num1 = Complex(1 , 3)
# num1.showNumber()        


# num2 = Complex(4 , 2)
# num2.showNumber()


# num3 = num1 + num2
# num3.showNumber()




# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return (22/7) * self.radius ** 2


#     def perimeter(self):
#         return 2 * (22/7) * self.radius


# c1 = Circle(21)
# print(c1.area() )
# print(c1.perimeter())    


# c2 = Circle(25)
# print(c2.area() )
# print(c2.perimeter())    d



# class Employee:
#     def __init__(self, role, dept, salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary

#     def showDetails(self):
#         print("role = ", self.role)
#         print('dept = ', self.dept)
#         print("salary = ", self.salary)


# class Eng(Employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__("Eng", "IT","100000")


# engg1 = Eng("Raj", "22")    
# engg1.showDetails()



class order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, ord2):
        return self.price > ord2.price


ord1 = order("chips", 20)
ord2 = order("tea", 15)

print(ord1 > ord2)