# class student:
#     name = "karan"
# s1 = student()
# print(s1.name)   


# class Car:
#     color = "blue"
#     brand = "tajj"

# car1 = Car()

# print(car1.brand)


# class student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
        
# s1 = student("karan", 98)
# print(s1.name, s1.marks)

# class student:
#     college_name = "abcd "
#     def __init__(self, name , marks):
#         self.name = name
#         self.marks = marks

#     def welcome(self):
#         print("welcome student", self.name)

#     def get_marks(self):
#         return self.marks    

# s1 = student("karan", 98)
# print(s1.name)      
# print(s1.college_name)  
# s1.welcome()
# print(s1.get_marks())

# class student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def marks_avg(self):
#         sum = 0
#         for value in self.marks: 
#             sum += value


#         print("hi", self.name, "avg markd", sum/3)   


# s1 = student("tony stark", [98,98, 95])         
# print(s1.name, s1.marks)
# s1.marks_avg()


# class car:
#     def __init__ (self):
#         self.acc = False
#         self.cultch = False
#         self.brk = False

#     def start(self):
#         self.cultch = True
#         self.acc = True
#         print("car start")

# c1 = car()
# c1.start()           



class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.accountno = acc

    def debit(self, amount):
        self.balance -= amount
        print("rs", amount, "debit")
        print("total balance", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("rs", amount, "credit")  
        print("total balance", self.get_balance())

    def get_balance(self):
        return self.balance          

acc1 = Account(100000, 12345)
acc1.debit(1000)
acc1.credit(10000)       