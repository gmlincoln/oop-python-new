# 🧠 Python OOP (Object Oriented Programming) – Complete Guide

This document explains Python OOP concepts from the very beginning to advanced level with examples and diagrams.

---

### 📌 What is OOP?

OOP (Object Oriented Programming) is a programming style where we organize code using:

- Classes
- Objects

It helps to build real-world structured and scalable applications.

---

### 1️⃣ Class

A class is a blueprint or template.

Example:

```python
class Student:
    pass
```

##### Student is just a design. It does not hold data ye


### 2️⃣ Object

An object is a real instance of a class.

```python

class Student:
    pass

s1 = Student()
s2 = Student()


```

- Student → Blueprint  
- s1, s2 → Real objects

### 3️⃣ Constructor (__init__)

A constructor runs automatically when an object is created.

```python

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Lincoln", 23)

print(s1.name)
print(s1.age)

```

#### Explanation

self.name = name

Left side → Object variable

Right side → Value passed during object creation


### 4️⃣ Instance Variables

Variables created using self inside constructor.

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

```

Each object will have its own separate data.


### 5️⃣ Methods

Functions inside a class are called methods.

```python 
class Calculator:
    def add(self, a, b):
        return a + b

obj = Calculator()
print(obj.add(5, 3))

```

### 6️⃣ Encapsulation
📌 Definition

Encapsulation means:

Protecting data and allowing controlled access.

```bash
        Bank Account
        -----------------
        - balance (private)
        -----------------
        + deposit()
        + withdraw()
        + get_balance()

```

#### 🔹 Example

```python
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount(5000)
account.deposit(1000)
print(account.get_balance())


```

❌ Direct access is not allowed:

```bash
account.__balance

```

### 7️⃣ Inheritance
📌 Definition

Inheritance means:

A child class can reuse properties and methods of a parent class.

Diagram: 

```lua 

            User
        ----------------
        + username
        + email
                ↑
                |
    -----------------------
    |                     |
 Customer              Admin


```

#### Example

```python

class User:
    def login(self):
        print("User Logged In")


class Admin(User):
    def delete_user(self):
        print("User Deleted")


admin = Admin()
admin.login()
admin.delete_user()


```

Admin inherits login() from User.



### 8️⃣ Method Overriding

Child class can modify parent method behavior.

```python

class Father:
    def show(self):
        print("Father Method")


class Son(Father):
    def show(self):
        print("Son Method")


obj = Son()
obj.show()

```

Output: 

```bash 

Son Method

```

### 9️⃣ Polymorphism
📌 Definition

Polymorphism means:

Same method name, different behavior.

Diagram: 
```bash
        Animal
        ---------
        + speak()
              ↑
     ------------------
     |                |
    Dog              Cat
  speak()          speak()
  "Bark"           "Meow"


```

#### Example

```python
class Dog:
    def speak(self):
        print("Bark")


class Cat:
    def speak(self):
        print("Meow")


for animal in [Dog(), Cat()]:
    animal.speak()



```


### 🔟 Abstraction

Abstraction means:

Hiding implementation details and forcing structure.

Diagram: 

```lua
        Abstract Class
        ----------------
            Shape
        ----------------
        + area() (abstract)
                ↑
                |
    -------------------------
    |                       |
 Rectangle              Circle


```

#### Example
```python

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


r = Rectangle(5, 10)
print(r.area())


```

❌ Cannot create object of abstract class:

```python

s = Shape()


```

### 🏛 The 4 Pillars of OOP

```lua

| Concept       | Purpose                         |
| ------------- | ------------------------------- |
| Encapsulation | Protect data                    |
| Inheritance   | Reuse code                      |
| Polymorphism  | Same method, different behavior |
| Abstraction   | Force structure                 |


```

### 🎯 Constructor vs Method Parameter
Use Constructor When:

Data is permanent (name, width, height)

Use Method Parameter When:

Data changes per operation (amount, message, discount)

Example:

```python

payment = BkashService()
payment.pay(user, 1000)


```